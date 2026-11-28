
import logging

from french_verb_trainer.services.answer_checker import AnswerChecker
from french_verb_trainer.services.exercise_service import ExerciseService


logger = logging.getLogger(__name__)


class ConsoleInterface:
    """Text-based user interface."""

    def __init__(
        self,
        exercise_service: ExerciseService,
        answer_checker: AnswerChecker,
    ) -> None:
        """Initialize the console interface with the required services."""
        self.exercise_service = exercise_service
        self.answer_checker = answer_checker

    def run(self) -> None:
        """Start the application."""
        logger.info('Training session started.')
        print('Welcome to French Verb Trainer!')

        while True:
            exercise = self.exercise_service.generate_exercise()
            logger.debug('New exercise generated.')

            print(f'\n{exercise.question}')

            user_answer = input("Your answer (or 'q' to quit): ")

            if user_answer.lower().strip() == 'q':
                logger.info('Training session ended by user.')
                print('Goodbye!')
                break

            is_correct = self.answer_checker.check(
                user_answer,
                exercise.correct_answer,
            )

            if is_correct:
                logger.info('User submitted a correct answer.')
                print('Correct!')
            else:
                logger.info('User submitted an incorrect answer.')
                print(f'Incorrect. Correct answer: {exercise.correct_answer}')
