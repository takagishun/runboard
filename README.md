# Minimal Val App

Tiny SQLite-backed Python app with a `vals` table, a small migration runner, and
a simple JSON endpoint.

## Run

```sh
python3 scripts/smoke.py
```

The script creates `.tmp/smoke.sqlite3`, applies all migrations in this branch,
seeds one val, and asks the application code to read it.

To run the demo server:

```sh
python3 scripts/reset_db.py
python3 -m app.server
```

Then open `http://127.0.0.1:8000/vals/1`.
