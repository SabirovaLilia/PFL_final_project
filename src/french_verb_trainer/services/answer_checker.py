"""
Answer check.
"""
class AnswerChecker:
    """
    User answers against expected conjugated forms check.
    """

    @staticmethod
    def normalize(answer: str) -> str: #TODO: decide how strict the answer check will be
        """
        Normalize an answer before comparison.
        """
        return answer.strip().lower().replace('’', "'")

    def check(self, user_answer: str, correct_answer: str) -> bool:
        """
        Return True if the user's answer is correct.
        """
        return (
            self.normalize(user_answer)
            == self.normalize(correct_answer)
        )
