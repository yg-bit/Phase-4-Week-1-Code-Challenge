# Flask Superheroes API

This repository is an implementation of the Phase 4 Week 1 Code Challenge "Superheroes" API.

Setup

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Seed the database:

```bash
python seed.py
```

4. Run the app:

```bash
python app.py
```

The app will run on `http://127.0.0.1:5000` by default.

Endpoints

- `GET /heroes` - list heroes (id, name, super_name)
- `GET /heroes/<id>` - show hero with nested `hero_powers` and `power`
- `GET /powers` - list powers
- `GET /powers/<id>` - show single power
- `PATCH /powers/<id>` - update a power's description (must be >= 20 chars)
- `POST /hero_powers` - create a hero_power. Body: `{ "strength": "Average", "power_id": 1, "hero_id": 3 }`

Notes

- The database uses SQLite at `superheroes.db` by default.
- Valid strengths: `Strong`, `Weak`, `Average`.
- `Power.description` must be at least 20 characters to pass validation when updating.
