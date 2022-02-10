from src.abc import CourseStore
from src.models import Course


class CourseServices:
    def __init__(self, course_store: CourseStore):
        self._course_store = course_store

    def get_course(self) -> Course:
        return self._course_store.get_course()

    def store_course(self, course: Course):
        self._course_store.create_course(course)
