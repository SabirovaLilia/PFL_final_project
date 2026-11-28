"""
Check ExerciseService:
- generating an exercise with an available verb;
- selecting an available voice, tense, and subject;
- checking for an error when no verbs are available;
- checking for an error when a verb has no conjugations.
"""

import pytest

from french_verb_trainer.models.verb import Verb
from french_verb_trainer.services.exercise_service import ExerciseService


class FakeVerbRepository:
    def __init__(self, verbs):
        self.verbs = verbs

    def get_all(self):
        return self.verbs


@pytest.fixture
def verb():
    return Verb(
        infinitive='parler',
        conjugations={
            'active': {
                'Présent': {
                    'je': 'parle',
                    'tu': 'parles',
                    'nous': 'parlons',
                },
                'Imparfait': {
                    'je': 'parlais',
                    'tu': 'parlais',
                },
            },
            'passive': {
                'Présent': {
                    'je': 'suis parlé',
                },
            },
        },
    )


@pytest.fixture
def service(verb):
    repository = FakeVerbRepository([verb])
    return ExerciseService(repository)


def test_generate_exercise_returns_exercise(service, verb):
    exercise = service.generate_exercise()

    assert exercise.verb == verb


def test_generate_exercise_uses_available_voice(service):
    exercise = service.generate_exercise()

    assert exercise.voice in ('active', 'passive')


def test_generate_exercise_uses_available_tense(service):
    exercise = service.generate_exercise()

    assert exercise.tense in ('Présent', 'Imparfait')


def test_generate_exercise_uses_available_subject(service):
    exercise = service.generate_exercise()

    available_subjects = {
        'je', 'tu', 'nous'
    }

    assert exercise.subject in available_subjects


def test_generate_exercise_raises_error_when_no_verbs():
    repository = FakeVerbRepository([])
    service = ExerciseService(repository)

    with pytest.raises(ValueError, match='No verbs available.'):
        service.generate_exercise()


def test_generate_exercise_raises_error_when_verb_has_no_conjugations():
    verb = Verb(
        infinitive='parler',
        conjugations={},
    )
    repository = FakeVerbRepository([verb])
    service = ExerciseService(repository)

    with pytest.raises(ValueError, match='No conjugations available for parler.'):
        service.generate_exercise()
