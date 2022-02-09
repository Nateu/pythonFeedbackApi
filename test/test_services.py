from typing import Optional

from src.abc import CourseStore
from src.models import Course
from src.services import CourseServices


class FakeCourseStore(CourseStore):
    def __init__(self, course: Optional[Course]):
        self._course = course

    def get_course(self) -> Optional[Course]:
        return self._course

    def create_course(self, course: Course):
        self._course = course


def test_get_course_returns_stored_course():
    # Given
    expected_course = Course(course_name="A")
    course_store = FakeCourseStore(course=expected_course)

    # When
    retrieved_course = CourseServices(course_store=course_store).get_course()

    # Then
    assert retrieved_course == expected_course
