"""
Check Verb class:
- obtaining the correct form;
- obtaining the form for another pronoun;
- obtaining the form from another tense;
- checking for an error when voice, tense, or subject is missing.
"""

import pytest

from french_verb_trainer.models.verb import Verb


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
                    'nous': 'parlions',
                },
            },
            'passive': {
                'Présent': {
                    'je': 'suis parlé',
                    'tu': 'es parlé',
                },
            },
        },
    )


def test_get_form_returns_correct_form(verb):
    assert verb.get_form('active', 'Présent', 'je') == 'parle'


def test_get_form_returns_correct_form_for_another_subject(verb):
    assert verb.get_form('active', 'Présent', 'nous') == 'parlons'


def test_get_form_returns_correct_form_for_another_tense(verb):
    assert verb.get_form('active', 'Imparfait', 'je') == 'parlais'


def test_get_form_raises_key_error_for_unknown_voice(verb):
    with pytest.raises(KeyError):
        verb.get_form('unknown', 'Présent', 'je')


def test_get_form_raises_key_error_for_unknown_tense(verb):
    with pytest.raises(KeyError):
        verb.get_form('active', 'Futur', 'je')


def test_get_form_raises_key_error_for_unknown_subject(verb):
    with pytest.raises(KeyError):
        verb.get_form('active', 'Présent', 'ils')
