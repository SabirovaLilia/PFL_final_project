"""Verb repository interface."""

from typing import Protocol

from french_verb_trainer.models.verb import Verb


class VerbRepository(Protocol):
    """Interface for accessing verb data."""

    def get_all(self) -> list[Verb]:
        """Return all available verbs."""
        ...
