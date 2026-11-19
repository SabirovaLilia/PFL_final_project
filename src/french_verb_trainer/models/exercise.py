"""
Task class.

Сontains a specific question: which verb, which tense, which pronoun.
Also keeps the correct answer to compare with user's one.

For question example, "Conjugate parler in Présent for nous", where:
- "parler" is a verb,
- "Présent" is a tense,
- and "nous" is a pronoun.

The correct answer for the example is "parlons".
"""
from dataclasses import dataclass

from french_verb_trainer.models.verb import Verb


@dataclass
class Exercise:
    """
    Conjugation exercise representation.
    """
    verb: Verb
    tense: str
    subject: str

    @property
    def question(self) -> str:
        """
        Build a human-readable exercise question.
        """
        return (
            f"Conjugate '{self.verb.infinitive}' "
            f"in {self.tense} for '{self.subject}'."
        )

    @property
    def correct_answer(self) -> str:
        """
        Return the expected answer.
        """
        return self.verb.get_form(self.tense, self.subject)
