"""French verb class."""

from dataclasses import dataclass


@dataclass
class Verb:
    """French verb and its conjugated forms representation."""

    infinitive: str
    conjugations: dict[str, dict[str, dict[str, str]]]
    # TODO: add DB guarantee or implement validation to avoid KerError

    def get_form(self, voice: str, tense: str, subject: str) -> str:
        """Return the conjugated form for a given tense and subject."""
        return self.conjugations[voice][tense][subject]
