from __future__ import annotations

import sys
import sqlite3
from pathlib import Path

MIGRATIONS_DIR = Path(__file__).resolve().parents[1] / "migrations"


def migrate(db_path: str | Path) -> None:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            create table if not exists schema_migrations (
              version text primary key
            )
            """
        )

        applied = {
            row[0]
            for row in conn.execute("select version from schema_migrations").fetchall()
        }

        for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
            if migration.name in applied:
                continue

            conn.executescript(migration.read_text())
            conn.execute(
                "insert into schema_migrations (version) values (?)",
                (migration.name,),
            )


if __name__ == "__main__":
    migrate(sys.argv[1] if len(sys.argv) > 1 else ".tmp/app.sqlite3")
