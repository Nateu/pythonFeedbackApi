from unittest.mock import mock_open, patch

from src.models import Course, Feedback
from src.stores import CourseStoreImpl, FeedbackStoreImpl


def test_create_course_writes_course_information_in_json():
    # Given
    course = Course(course_name="TEST")
    # When
    with patch("builtins.open", new_callable=mock_open) as mocked_open:
        CourseStoreImpl().create_course(course=course)
    # Then
    mocked_open.return_value.write.assert_called_once_with('{"course_name": "TEST"}')


def test_add_feedback_appends_feedback_to_already_existing_list():
    # Given
    feedback = Feedback(name="C", score=10, comment="T")
    # When
    with patch(
        "builtins.open",
        new=mock_open(
            read_data='[{"name": "A", "score": 5, "comment": "T"}, {"name": "B", "score": 7, "comment": "T"}]'
        ),
    ) as mocked_open:
        FeedbackStoreImpl().add_feedback(feedback=feedback)
    # Then
    mocked_open.return_value.write.assert_called_once_with(
        '[{"name": "A", "score": 5, "comment": "T"}, {"name": "B", "score": 7, "comment": "T"}, {"name": "C", "score": 10, "comment": "T"}]'
    )
