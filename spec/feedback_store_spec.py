from unittest.mock import Mock, mock_open, patch

from expects import equal, expect
from mamba import context, describe, it

from src.models import Feedback
from src.stores import FeedbackStoreImpl


with describe("Given a feedback store") as self:
    with context("when feedback is added"):
        with it("should append feedback to already existing list"):
            feedback = Feedback(name="C", score=10, comment="T")
            with patch(
                "builtins.open",
                new=mock_open(
                    read_data='[{"name": "A", "score": 5, "comment": "T"}, {"name": "B", "score": 7, "comment": "T"}]'
                ),
            ) as mocked_open:
                FeedbackStoreImpl().add_feedback(feedback=feedback)
            mocked_open.return_value.write.assert_called_once_with(
                '[{"name": "A", "score": 5, "comment": "T"}, {"name": "B", "score": 7, "comment": "T"}, {"name": "C", "score": 10, "comment": "T"}]'
            )

    with context("when feedback is not stored yet"):
        with context("and you try to retrieve feedback"):
            with it("should return an empty list"):
                with patch(
                    "builtins.open",
                    new=Mock(side_effect=FileNotFoundError()),
                ) as mocked_open:
                    result = FeedbackStoreImpl().get_feedback()
                expect(isinstance(mocked_open.side_effect, FileNotFoundError)).to(equal(True))
                expect(result).to(equal([]))

    with context("when some feedback is stored already"):
        with context("and you try to retrieve feedback"):
            with it("should return list with feedback"):
                with patch(
                    "builtins.open",
                    new=mock_open(
                        read_data='[{"name": "A", "score": 5, "comment": "T"}, {"name": "B", "score": 7, "comment": "T"}, {"name": "C", "score": 10, "comment": "T"}]'
                    ),
                ) as mocked_open:
                    feedback = FeedbackStoreImpl().get_feedback()
                expect(feedback[0].json()).to(equal('{"name": "A", "score": 5, "comment": "T"}'))
