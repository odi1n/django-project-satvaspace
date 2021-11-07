FROM python:3.9

# set environment variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV POETRY_VERSION=1.1.11

# update pip
RUN pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION"

# set work directory
WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml entrypoint.sh /usr/src/app/

RUN poetry config virtualenvs.create false \
    && poetry install  --no-interaction --no-ansi

COPY . /usr/src/app

RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]