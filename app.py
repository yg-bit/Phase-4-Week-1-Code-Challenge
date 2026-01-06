from flask import Flask, jsonify, request
from flask_migrate import Migrate
from config import Config
from models import db, Hero, Power, HeroPower



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([h.to_dict() for h in heroes]), 200

    @app.route('/heroes/<int:hero_id>', methods=['GET'])
    def get_hero(hero_id):
        hero = Hero.query.get(hero_id)
        if not hero:
            return jsonify({'error': 'Hero not found'}), 404

        # serialize hero with hero_powers including nested power
        hp_list = []
        for hp in hero.hero_powers:
            hp_list.append({
                'id': hp.id,
                'hero_id': hp.hero_id,
                'power_id': hp.power_id,
                'strength': hp.strength,
                'power': hp.power.to_dict() if hp.power else None
            })

        result = hero.to_dict()
        result['hero_powers'] = hp_list
        return jsonify(result), 200

    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([p.to_dict() for p in powers]), 200

    @app.route('/powers/<int:power_id>', methods=['GET'])
    def get_power(power_id):
        p = Power.query.get(power_id)
        if not p:
            return jsonify({'error': 'Power not found'}), 404
        return jsonify(p.to_dict()), 200

    @app.route('/powers/<int:power_id>', methods=['PATCH'])
    def patch_power(power_id):
        p = Power.query.get(power_id)
        if not p:
            return jsonify({'error': 'Power not found'}), 404

        data = request.get_json() or {}
        description = data.get('description')
        if description is None:
            return jsonify({'errors': ['description is required']}), 400
        if len(description) < 20:
            return jsonify({'errors': ['description must be at least 20 characters long']}), 400

        p.description = description
        db.session.add(p)
        db.session.commit()
        return jsonify(p.to_dict()), 200

    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.get_json() or {}
        strength = data.get('strength')
        power_id = data.get('power_id')
        hero_id = data.get('hero_id')

        errors = []
        if strength not in HeroPower.VALID_STRENGTHS:
            errors.append("strength must be one of 'Strong', 'Weak', 'Average'")

        hero = Hero.query.get(hero_id) if hero_id is not None else None
        power = Power.query.get(power_id) if power_id is not None else None
        if not hero:
            errors.append('hero must exist')
        if not power:
            errors.append('power must exist')

        if errors:
            return jsonify({'errors': errors}), 400

        hp = HeroPower(hero_id=hero.id, power_id=power.id, strength=strength)
        db.session.add(hp)
        db.session.commit()

        result = hp.to_dict()
        result['hero'] = hero.to_dict()
        result['power'] = power.to_dict()
        return jsonify(result), 201

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
