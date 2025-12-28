from app import create_app
from models import db, Hero, Power, HeroPower


def seed():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()


        heroes = [
            ('Kamala Khan', 'Ms. Marvel'),
            ('Doreen Green', 'Squirrel Girl'),
            ('Gwen Stacy', 'Spider-Gwen'),
            ('Janet Van Dyne', 'The Wasp'),
            ('Wanda Maximoff', 'Scarlet Witch'),
            ('Carol Danvers', 'Captain Marvel'),
            ('Jean Grey', 'Dark Phoenix'),
            ('Ororo Munroe', 'Storm'),
            ('Kitty Pryde', 'Shadowcat'),
            ('Elektra Natchios', 'Elektra'),
        ]

        hero_objs = []
        for name, super_name in heroes:
            h = Hero(name=name, super_name=super_name)
            db.session.add(h)
            hero_objs.append(h)

    
        powers = [
            ('super strength', 'gives the wielder super-human strengths'),
            ('flight', 'gives the wielder the ability to fly through the skies at supersonic speed'),
            ('super human senses', 'allows the wielder to use her senses at a super-human level'),
            ('elasticity', 'can stretch the human body to extreme lengths'),
        ]

        power_objs = []
        for name, desc in powers:
            p = Power(name=name, description=desc)
            db.session.add(p)
            power_objs.append(p)

        db.session.commit()

        
        hps = [
            (1, 2, 'Strong'),
            (1, 1, 'Weak'),
            (3, 1, 'Average')
        ]
        for hero_id, power_id, strength in hps:
            hp = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
            db.session.add(hp)

        db.session.commit()
        print('Seeded database')


if __name__ == '__main__':
    seed()
