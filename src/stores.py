from typing import List, Optional

from pydantic import parse_raw_as

from src.abc import CourseStore, FeedbackStore
from src.models import Course, Feedback


class CourseStoreImpl(CourseStore):
    def create_course(self, course: Course):
        with open("courses.json", "w") as fp:
            fp.write(course.json())

    def get_course(self) -> Optional[Course]:
        try:
            with open("courses.json", "r") as fp:
                json_string: str = fp.read()
            return Course.parse_raw(json_string)
        except FileNotFoundError:
            return None


class FeedbackStoreImpl(FeedbackStore):
    def add_feedback(self, feedback: Feedback):
        with open("feedback.json", "r+") as fp:
            data = fp.read()
            data = parse_raw_as(List[Feedback], data)
            data.append(feedback)
            fp.write(f"[{', '.join([f.json() for f in data])}]")

    def get_feedback(self) -> List[Feedback]:
        try:
            with open("feedback.json", "r") as fp:
                data = fp.read()
            return parse_raw_as(List[Feedback], data)
        except FileNotFoundError:
            return []
