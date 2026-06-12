from __future__ import annotations

import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = Path(".tmp/app.sqlite3")


def connect(db_path: str | Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_val(val_id: int, db_path: str | Path = DEFAULT_DB_PATH) -> dict[str, object]:
    with connect(db_path) as conn:
        row = conn.execute(
            """
            select vals.id, owner_profiles.display_name, vals.code
            from vals
            join owner_profiles on owner_profiles.val_id = vals.id
            where vals.id = ?
            """,
            (val_id,),
        ).fetchone()

    if row is None:
        raise LookupError(f"val {val_id} not found")

    return {
        "id": row["id"],
        "owner": row["display_name"],
        "code": row["code"],
    }
