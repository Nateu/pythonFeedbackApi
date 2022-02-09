from src.abc import CourseStore


class CourseServices:
    def __init__(self, course_store: CourseStore):
        self._course_store = course_store

    def get_course(self):
        pass

    def store_course(self):
        pass
