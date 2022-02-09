from fastapi import FastAPI


feedback_api = FastAPI()


@feedback_api.get("/")
async def root():
    return "FastAPI Works!"
