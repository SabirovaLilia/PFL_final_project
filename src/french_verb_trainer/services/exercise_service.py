"""Tasks creation and assignment."""

import random

from french_verb_trainer.models.exercise import Exercise
from french_verb_trainer.repositories.verb_repository import VerbRepository


class ExerciseService:
    """Conjugation exercises generator."""

    def __init__(self, repository: VerbRepository) -> None:
        """Initialize the service with a verb repository."""
        self.repository = repository

    def generate_exercise(self) -> Exercise:
        """Create a random conjugation exercise."""
        verbs = self.repository.get_all()

        if not verbs:
            raise ValueError('No verbs available.')

        verb = random.choice(verbs)

        if not verb.conjugations:
            raise ValueError(f'No conjugations available for {verb.infinitive}.')

        voice = random.choice(list(verb.conjugations.keys()))
        tense = random.choice(list(verb.conjugations[voice].keys()))
        subject = random.choice(list(verb.conjugations[voice][tense].keys()))

        return Exercise(
            verb=verb,
            voice=voice,
            tense=tense,
            subject=subject,
        )
