from typing import List, Optional

from expects import equal, expect
from mamba import before, context, describe, it

from src.abc import FeedbackStore
from src.models import Feedback
from src.services import FeedbackServices


class FakeFeedbackStore(FeedbackStore):
    def __init__(self, feedback: Optional[Feedback]):
        if feedback:
            self._feedback: List[Feedback] = [feedback]
        else:
            self._feedback: List[Feedback] = []

    def get_feedback(self) -> List[Feedback]:
        return self._feedback

    def add_feedback(self, feedback: Feedback):
        if self._feedback:
            self._feedback.append(feedback)
        else:
            self._feedback = [feedback]


with describe("Given a feedback service") as self:
    with context("when the feedback store is empty"):
        with context("and you store feedback"):
            with it("should store this feedback"):
                feedback_store = FakeFeedbackStore(feedback=None)
                feedback_service = FeedbackServices(feedback_store=feedback_store)
                expected_feedback = Feedback(name="Pascal", score=5, comment="Loved it!")
                feedback_service.add_feedback(expected_feedback)
                expect(feedback_store.get_feedback()[0]).to(equal(expected_feedback))

    with context("when the feedback store is not empty"):
        with before.each:
            self.expected_feedback = Feedback(name="A", score=2, comment="it's okay")
            self.feedback_store = FakeFeedbackStore(feedback=Feedback(name="A", score=2, comment="it's okay"))
            self.feedback_store.add_feedback(feedback=Feedback(name="B", score=4, comment="it's better than okay"))
            self.feedback_service = FeedbackServices(feedback_store=self.feedback_store)

        with context("and you store feedback"):
            with it("should store this feedback and keep the original feedback"):
                expected_feedback = Feedback(name="C", score=10, comment="Loved it!")
                self.feedback_service.add_feedback(expected_feedback)
                expect(self.feedback_store.get_feedback()[2]).to(equal(expected_feedback))

        with context("and you retrieve feedback"):
            with it("should provide the feedback already contained"):
                expect(self.feedback_service.get_feedback()[0]).to(equal(self.expected_feedback))
