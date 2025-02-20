FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app

RUN poetry add python-dotenv

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "poetry run python -m dotenv main.py"]