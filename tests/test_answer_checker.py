"""
Check:
- identical answers are considered correct;
- answers with different cases are considered the same;
- extra spaces at the beginning and end do not affect the result;
- an incorrect answer is considered incorrect;
- French apostrophes of different types are normalized in the same way.
"""

import pytest

from french_verb_trainer.services.answer_checker import AnswerChecker


@pytest.fixture
def checker():
    return AnswerChecker()


@pytest.mark.parametrize(
    ('user_answer', 'correct_answer', 'expected'),
    [
        ('parle', 'parle', True),
        ('PARLE', 'parle', True),
        ('  parle  ', 'parle', True),
        ("j'aime", "j’aime", True),
        ('parles', 'parle', False),
        ('', 'parle', False),
    ],
)
def test_check_answer(checker, user_answer, correct_answer, expected):
    assert checker.check(user_answer, correct_answer) is expected
