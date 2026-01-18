# Phase-4-Week-1-Code-Challenge

Flask API for managing Heroes and Powers backed by SQLAlchemy.

Requirements
- Python 3.8+
- pip or pipenv

Install (pipenv)

```bash
pipenv install --dev
pipenv shell
```

Install (pip)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Configuration
- By default the app uses SQLite at `superheroes.db` in the project root.
- To use another database, set `DATABASE_URL` in the environment.

Run (development)

```bash
python app.py
# or with the flask CLI
flask run
```

The server listens on `http://127.0.0.1:5000` by default.

Database & migrations

Uses `flask-migrate` (Alembic). Common commands:

```bash
# initialize migrations (only once)
flask db init
flask db migrate -m "message"
flask db upgrade
```

Seeding

Run the included seeding script:

```bash
python seed.py
```

API endpoints

- `GET /heroes` — list heroes
- `GET /heroes/<id>` — hero with `hero_powers`
- `GET /powers` — list powers
- `GET /powers/<id>` — get power
- `PATCH /powers/<id>` — update `description` (min 20 chars)
- `POST /hero_powers` — create association (body: `hero_id`, `power_id`, `strength` — one of `Strong`, `Weak`, `Average`)

Example request

```json
POST /hero_powers
{
  "hero_id": 1,
  "power_id": 2,
  "strength": "Strong"
}
```

This README contains setup and usage notes for the project.
