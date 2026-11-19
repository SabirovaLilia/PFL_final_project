"""Temporary in-memory verb repository."""

from french_verb_trainer.models.verb import Verb


class InMemoryVerbRepository:
    """Temporary repository for storing verbs in memory."""

    def __init__(self) -> None:
        """Initialize the repository with sample verb data."""
        self._verbs = [
            Verb(
                infinitive='parler',
                translation='to speak',
                group=1,
                conjugations={
                    'Présent': {
                        'je': 'parle',
                        'tu': 'parles',
                        'il/elle/on': 'parle',
                        'nous': 'parlons',
                        'vous': 'parlez',
                        'ils/elles': 'parlent',
                    }
                },
            ),
            Verb(
                infinitive='finir',
                translation='to finish',
                group=2,
                conjugations={
                    'Présent': {
                        'je': 'finis',
                        'tu': 'finis',
                        'il/elle/on': 'finit',
                        'nous': 'finissons',
                        'vous': 'finissez',
                        'ils/elles': 'finissent',
                    }
                },
            ),
        ]

    def get_all(self) -> list[Verb]:
        """Return all available verbs."""
        return self._verbs
