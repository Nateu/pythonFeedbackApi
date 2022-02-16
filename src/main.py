from fastapi import FastAPI

from src.services import CourseServices, FeedbackServices
from src.stores import CourseStoreImpl, FeedbackStoreImpl


feedback_api = FastAPI()
course_services = CourseServices(course_store=CourseStoreImpl())
feedback_services = FeedbackServices(feedback_store=FeedbackStoreImpl())


@feedback_api.get("/")
async def root():
    return "FastAPI Works!"


@feedback_api.get("/course/")
async def something():
    return course_services.get_course()
