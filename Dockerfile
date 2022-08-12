FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user
ARG UID=1000

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} --uid=${UID} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./manage.py manage.py
COPY --chown=${USER} ./core core
COPY --chown=${USER} ./email_generator email_generator

USER ${USER}
