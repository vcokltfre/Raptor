FROM python:3.8

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml /app
COPY poetry.lock /app

RUN poetry install

COPY . /app

RUN poetry run aerich upgrade

CMD ["poetry", "run", "task", "start-api"]
