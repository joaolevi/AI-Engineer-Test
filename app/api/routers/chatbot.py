"""Package imports"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import logging
import os

"""App imports"""
from app.settings import init_settings

logger = logging.getLogger("uvicorn")

llm = init_settings()
prompt = os.getenv("PROMPT")

chatbot_classifier = r = APIRouter()
    
class QuestionRequest(BaseModel):
    question: str

def classify_question_llm(question: str):
    response = llm.invoke(prompt + "\n" + question)
    logger.info(response)
    response = response.strip("\n")
    return response

@r.post("/chatbot")
async def classify_question_endpoint(request: QuestionRequest):
    logger.info(f"Recebendo pergunta: {request.question}")
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="A pergunta não pode estar vazia.")
    
    question_type = classify_question_llm(request.question)
    return {"type": question_type}
