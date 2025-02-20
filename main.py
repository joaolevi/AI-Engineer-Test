from dotenv import load_dotenv

load_dotenv()

import logging
import os
import uvicorn
from fastapi import FastAPI
from app.api.routers.chatbot import chatbot_classifier
from app.settings import init_settings

app = FastAPI()

init_settings()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("uvicorn")

app.include_router(chatbot_classifier)

if __name__ == "__main__":
    app_host = os.getenv("APP_HOST", "0.0.0.0")
    app_port = int(os.getenv("APP_PORT", "8000"))

    uvicorn.run(app="main:app", host=app_host, port=app_port)
