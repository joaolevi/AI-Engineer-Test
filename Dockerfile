FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

COPY . /app

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["poetry", "run", "python", "main.py"]
