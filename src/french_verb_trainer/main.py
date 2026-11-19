"""Entry point for the trainer."""
from french_verb_trainer.gui.temp_interface import ConsoleInterface
from french_verb_trainer.repositories.in_memory_verb_repository import \
    InMemoryVerbRepository
from french_verb_trainer.services.answer_checker import AnswerChecker
from french_verb_trainer.services.exercise_service import ExerciseService


def main() -> None:
    repository = InMemoryVerbRepository()
    exercise_service = ExerciseService(repository)
    answer_checker = AnswerChecker()

    interface = ConsoleInterface(
        exercise_service=exercise_service,
        answer_checker=answer_checker,
    )

    interface.run()


if __name__ == '__main__':
    main()
