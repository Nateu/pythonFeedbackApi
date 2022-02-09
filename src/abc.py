from abc import ABC, abstractmethod

from src.models import Course, Feedback


class CourseStore(ABC):
    @abstractmethod
    def create_course(self, course: Course):
        pass

    @abstractmethod
    def get_course(self):
        pass


class FeedbackStore(ABC):
    @abstractmethod
    def add_feedback(self, feedback: Feedback):
        pass

    @abstractmethod
    def get_feedback(self):
        pass
