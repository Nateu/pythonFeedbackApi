from src.abc import CourseStore, FeedbackStore
from src.models import Course, Feedback


class CourseServices:
    def __init__(self, course_store: CourseStore):
        self._course_store = course_store

    def get_course(self) -> Course:
        return self._course_store.get_course()

    def store_course(self, course: Course):
        self._course_store.create_course(course)


class FeedbackServices:
    def __init__(self, feedback_store: FeedbackStore):
        self._feedback_store = feedback_store

    def add_feedback(self, feedback: Feedback):
        self._feedback_store.add_feedback(feedback=feedback)

    def get_feedback(self):
        return self._feedback_store.get_feedback()
