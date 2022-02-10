from unittest.mock import Mock, mock_open, patch

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


def test_course_does_not_exists_when_you_get_course_return_nothing():
    # Given
    # When
    with patch(
        "builtins.open",
        new=Mock(side_effect=FileNotFoundError()),
    ) as mocked_open:
        result = CourseStoreImpl().get_course()
    # Then
    assert isinstance(mocked_open.side_effect, FileNotFoundError)
    assert result is None


def test_course_does_exists_when_you_get_course_return_the_course():
    # Given
    # When
    with patch(
        "builtins.open",
        new=mock_open(read_data='{"courseName": "Feedback course"}'),
    ) as mocked_open:
        course: Course = CourseStoreImpl().get_course()
    # Then
    assert course.course_name == "Feedback course"


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


def test_feedback_store_is_empty_return_empty_list():
    # Given
    # When
    with patch(
        "builtins.open",
        new=Mock(side_effect=FileNotFoundError()),
    ) as mocked_open:
        result = FeedbackStoreImpl().get_feedback()
    # Then
    assert isinstance(mocked_open.side_effect, FileNotFoundError)
    assert result == []


def test_feedback_is_added_to_existing_feedback_return_appended_list():
    with patch(
        "builtins.open",
        new=mock_open(
            read_data='[{"name": "A", "score": 5, "comment": "T"}, {"name": "B", "score": 7, "comment": "T"}, {"name": "C", "score": 10, "comment": "T"}]'
        ),
    ) as mocked_open:
        feedback = FeedbackStoreImpl().get_feedback()
    json = f"[{', '.join([f.json() for f in feedback])}]"
    assert (
        json
        == '[{"name": "A", "score": 5, "comment": "T"}, {"name": "B", "score": 7, "comment": "T"}, {"name": "C", "score": 10, "comment": "T"}]'
    )
