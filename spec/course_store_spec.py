from unittest.mock import Mock, mock_open, patch

from expects import equal, expect
from mamba import context, describe, it

from src.models import Course
from src.stores import CourseStoreImpl


with describe("Given a course store") as self:
    with context("when a course is created"):
        with it("should write the course information in json"):
            course = Course(course_name="TEST")
            with patch("builtins.open", new_callable=mock_open) as mocked_open:
                CourseStoreImpl().create_course(course=course)
            mocked_open.return_value.write.assert_called_once_with('{"course_name": "TEST"}')

    with context("when a course doesn't exists"):
        with context("and you try to get the course info"):
            with it("should return nothing"):
                with patch(
                    "builtins.open",
                    new=Mock(side_effect=FileNotFoundError()),
                ) as mocked_open:
                    result = CourseStoreImpl().get_course()
                expect(isinstance(mocked_open.side_effect, FileNotFoundError)).to(equal(True))
                expect(result).to(equal(None))

    with context("when a course does exists"):
        with context("and you try to get the course info"):
            with it("should return the course name"):
                with patch(
                    "builtins.open",
                    new=mock_open(read_data='{"courseName": "Feedback course"}'),
                ) as mocked_open:
                    course: Course = CourseStoreImpl().get_course()
                expect(course.course_name).to(equal("Feedback course"))
