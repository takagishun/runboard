from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.db import get_val
from reset_db import reset_db

DB_PATH = Path(".tmp/smoke.sqlite3")


def main() -> None:
    reset_db(DB_PATH)
    val = get_val(1, DB_PATH)
    print(json.dumps(val, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
