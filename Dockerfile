
FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY . /app

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

CMD ["poetry", "run", "python", "shifttask/main.py"]
