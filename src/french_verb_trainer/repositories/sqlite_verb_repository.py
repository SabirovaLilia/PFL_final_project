import sqlite3
from pathlib import Path

from french_verb_trainer.models.verb import Verb
from french_verb_trainer.repositories.verb_repository import VerbRepository

PERSON_MAP = {
    '1sm': 'je',
    '1sf': 'je',
    '2sm': 'tu',
    '2sf': 'tu',
    '3sm': 'il',
    '3sf': 'elle',
    '1p': 'nous',
    '2p': 'vous',
    '3pm': 'ils',
    '3pf': 'elles',
}

TIME_MAP = {
    ('indicatif', 'present'): 'Présent',
    ('indicatif', 'imparfait'): 'Imparfait',
    ('indicatif', 'futur_simple'): 'Futur simple',
    ('indicatif', 'passe_simple'): 'Passé simple',
    ('indicatif', 'passe_compose'): 'Passé composé',
    ('subjonctif', 'present'): 'Subjonctif présent',
    ('conditionnel', 'present'): 'Conditionnel présent',
    ('imperatif', 'present'): 'Impératif présent',
}

VOICE_NORMALIZER = {
    'voix_active_avoir': 'active',
    'voix_active_etre': 'active',
    'voix_active': 'active',
    'voix_passive': 'passive',
}


class SqliteVerbRepository(VerbRepository):
    """Interface for accessing verb data."""

    def __init__(self, db_path: Path | None = None) -> None:
        """Initialize the repository"""
        if db_path is None:
            self._db_path = Path("data/verbs.db")
        else:
            self._db_path = db_path

    def get_all(self) -> list[Verb]:
        """Return all available verbs."""
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT id, infinitif FROM verbes')
        verbs = []
        for verb_id, infinitif in cursor.fetchall():
            conjugations = self._load_conjugations(cursor, verb_id)
            verbs.append(
                Verb(
                    infinitive=infinitif,
                    conjugations=conjugations,
                )
            )

        conn.close()
        return verbs

    def _load_conjugations(self, cursor: sqlite3.Cursor, verb_id: int) -> dict[str, dict[str, str]]:
        cursor.execute(
            'SELECT voix, mode, temps, personne, conjugaison '
            'FROM conjugaisons WHERE verbe_id = ?',
            (verb_id,),
        )
        result = {}
        for voix, mode, temps, personne, form in cursor.fetchall():
            normalized_voice = VOICE_NORMALIZER.get(voix)
            if not normalized_voice:
                continue

            time_name = TIME_MAP.get((mode, temps))
            if not time_name:
                continue

            if normalized_voice not in result:
                result[normalized_voice] = {}
            if time_name not in result[normalized_voice]:
                result[normalized_voice][time_name] = {}

            person_key = personne.split(";")[0]
            subject = PERSON_MAP.get(person_key)
            if subject:
                result[normalized_voice][time_name][subject] = form

        return result
