#!/usr/bin/env bash
poetry run uvicorn src.main:feedback_api --port 7000 --reload