"""
Console interface.
 
Interaction with the user:
- display questions;
- receive answers;
- show the test result;
- manage a simple exercise execution cycle.
"""
from french_verb_trainer.services.answer_checker import AnswerChecker
from french_verb_trainer.services.exercise_service import ExerciseService


class ConsoleInterface:
    """
    Text-based user interface.
    """

    def __init__(
        self,
        exercise_service: ExerciseService,
        answer_checker: AnswerChecker,
    ) -> None:
        self.exercise_service = exercise_service
        self.answer_checker = answer_checker

    def run(self) -> None:
        """
        Start the application.
        """
        print("Welcome to French Verb Trainer!")

        while True:
            exercise = self.exercise_service.generate_exercise()

            print(f"\n{exercise.question}")

            user_answer = input("Your answer (or 'q' to quit): ")

            if user_answer.lower().strip() == "q":
                print("Goodbye!")
                break

            is_correct = self.answer_checker.check(
                user_answer,
                exercise.correct_answer,
            )

            if is_correct:
                print("Correct!")
            else:
                print(
                    f"Incorrect. Correct answer: "
                    f"{exercise.correct_answer}"
                )
