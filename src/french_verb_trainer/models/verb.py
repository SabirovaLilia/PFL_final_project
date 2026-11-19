"""French verb class."""
from dataclasses import dataclass


@dataclass
class Verb:
    """French verb and its conjugated forms representation."""

    infinitive: str
    translation: str
    group: int
    conjugations: dict[str, dict[str, str]] #TODO: add DB guarantee or implement validation to avoid KerError

    def get_form(self, tense: str, subject: str) -> str:
        """Return the conjugated form for a given tense and subject."""
        return self.conjugations[tense][subject]
