"""Package imports"""
import pytest
import pandas as pd
import os

from httpx import AsyncClient
from dotenv import load_dotenv

load_dotenv()

TEST_FILE_PATH = os.getenv("TEST_FILE_PATH")
SHEET_NAME = os.getenv("SHEET_NAME")

df = pd.read_excel(TEST_FILE_PATH, sheet_name="Página1")

@pytest.mark.asyncio
@pytest.mark.parametrize("question, expected_type", df.values.tolist())
async def test_api_responses(question, expected_type):
    """
    Envia perguntas para a API e valida se a resposta retorna o type correto.
    """
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.post("/chatbot", json={"question": question})

    assert response.status_code == 200, f"Erro na API para: {question}"
    response_json = response.json()
    
    assert "type" in response_json, f"Campo 'type' ausente na resposta da API para: {question}"
    assert response_json["type"] == expected_type, (
        f"Esperado: {expected_type}, Obtido: {response_json['type']} para pergunta: {question}"
    )
