"""Entry point for the trainer."""

from pathlib import Path

from french_verb_trainer.logging_config import setup_logging
from french_verb_trainer.data_loader import load_database
from french_verb_trainer.gui.temp_interface import ConsoleInterface
from french_verb_trainer.repositories.sqlite_verb_repository import SqliteVerbRepository
from french_verb_trainer.services.answer_checker import AnswerChecker
from french_verb_trainer.services.exercise_service import ExerciseService


def main() -> None:
    setup_logging()
    db_path = Path(__file__).parent.parent.parent / 'data' / 'verbs.db'
    load_database(db_path)
    repository = SqliteVerbRepository(db_path)
    exercise_service = ExerciseService(repository)
    answer_checker = AnswerChecker()

    interface = ConsoleInterface(
        exercise_service=exercise_service,
        answer_checker=answer_checker,
    )

    interface.run()


if __name__ == '__main__':
    main()
