import os

def init_settings():
    model_provider = os.getenv("MODEL_PROVIDER")
    model_name = os.getenv("MODEL")

    if not model_provider or not model_name:
        raise ValueError("As variáveis de ambiente MODEL e MODEL_PROVIDER devem ser definidas.")

    match model_provider:
        case "openai":
            from langchain_openai import OpenAI
            
            llm = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),
                model = os.getenv("MODEL", "gpt-3.5-turbo"),
                temperature=float(os.getenv("TEMPERATURE", "0.5")),
                max_tokens=int(os.getenv("MAX_TOKENS", "100")),
                max_retries=int(os.getenv("MAX_RETRIES", "3")),
            )
        case "ollama":
            from langchain_community.llms import Ollama

            llm = Ollama(model=model_name)
        case _:
            raise ValueError(f"Provedor de modelo inválido: {model_provider}")
    return llm
