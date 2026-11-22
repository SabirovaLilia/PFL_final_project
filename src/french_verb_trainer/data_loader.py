from pathlib import Path

import requests

url = 'https://github.com/ShingZhanho/verbe-conjugaison-academie-francaise/releases/download/v0.5.0/verbs.db'


def load_database(db_path: Path) -> None:
    """Download the database."""
    if db_path.exists():
        return

    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f'Cannot download database. Error: {e}')

    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.write_bytes(response.content)
