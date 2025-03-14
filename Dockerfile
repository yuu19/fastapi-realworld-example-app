FROM python:3.9.10-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8001
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

COPY . ./

CMD poetry run alembic upgrade head && \
    poetry run uvicorn --host=0.0.0.0 --port=8001 app.main:app
