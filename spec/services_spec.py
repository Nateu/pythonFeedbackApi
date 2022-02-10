from typing import Optional

from expects import equal, expect
from mamba import before, context, describe, it

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


with describe("Given a course service") as self:
    with before.each:
        self.expected_course = Course(course_name="A")

    with context("when the course store is empty"):
        with before.each:
            self.course_store = FakeCourseStore(course=None)

        with context("and you store a course"):
            with it("should return the newly stored course"):
                course_service = CourseServices(course_store=self.course_store)
                course_service.store_course(self.expected_course)
                retrieved_course = course_service.get_course()
                expect(retrieved_course).to(equal(self.expected_course))

        with context("and you get a course"):
            with it("should return nothing"):
                retrieved_course = CourseServices(course_store=self.course_store).get_course()
                expect(retrieved_course).to(equal(None))

    with context("when the course store is not empty"):
        with before.each:
            self.existing_course = Course(course_name="Existing course")
            self.course_store = FakeCourseStore(course=self.existing_course)

        with context("and you get a course"):
            with it("should return the stored course"):
                retrieved_course = CourseServices(course_store=self.course_store).get_course()
                expect(retrieved_course).to(equal(self.existing_course))

        with context("and you store a course"):
            with it("should return the newly stored course"):
                new_course = Course(course_name="New")
                course_service = CourseServices(course_store=self.course_store)
                course_service.store_course(new_course)
                expect(course_service.get_course()).to(equal(new_course))
