from __future__ import annotations

import sqlite3
from pathlib import Path

from migrate import migrate

DEFAULT_DB_PATH = Path(".tmp/app.sqlite3")


def reset_db(db_path: str | Path = DEFAULT_DB_PATH) -> None:
    db_path = Path(db_path)
    db_path.unlink(missing_ok=True)
    migrate(db_path)
    seed(db_path)


def seed(db_path: str | Path) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "insert into vals (id, code) values (?, ?)",
            (1, "export const hello = 'world';"),
        )
        conn.execute(
            "insert into owner_profiles (val_id, display_name) values (?, ?)",
            (1, "sophie"),
        )


if __name__ == "__main__":
    reset_db()
    print(f"reset {DEFAULT_DB_PATH}")
