# from expects import equal, expect
# from mamba import before, context, describe, it
# from fastapi import FastAPI
# from fastapi.testclient import TestClient


# from src.main import feedback_api
#
#
# client = TestClient(feedback_api)
#
# with _describe("Given a feedback api end point /course/") as self:
#     with context("when get the course "):
#         with it("should return the course that is stored"):
#             response = client.get("/course/")
#             assert response.status_code == 200
#             assert response.json() == {"msg": "Hello World"}
