ARG PYTHON_VERSION=3.8.6-alpine3.12

# Python base image
FROM python:${PYTHON_VERSION} AS urbandata-python38-base

WORKDIR /wheels

COPY requirements.txt requirements_dev.txt ./

RUN set -x \
    && apk add --no-cache --virtual build-dependencies \
        g++ \
        libffi-dev \
        postgresql-dev \
    # Generating wheels
    && pip install --upgrade pip \
    && pip wheel -r /wheels/requirements_dev.txt \
    # Cleaning up image
    && rm -rf /root/.cache \
    && apk del build-dependencies


# Service production image
FROM python:${PYTHON_VERSION} AS urbandata-test-prod


COPY --from=urbandata-python38-base /wheels /wheels

RUN set -x \
    && apk add --no-cache \
        libpq \
        mailcap \
    # Installing dependencies
    && pip install --upgrade pip \
    && pip install -r /wheels/requirements.txt -f /wheels \
    # Cleaning up image
    && rm -rf /wheels \
    && rm -rf /root/.cache

# Creating app's user/group
RUN addgroup -S appgroup \
    && adduser -S -h /home/appuser appuser appgroup \
    # Some extra initialization
    && mkdir -p /var/log/uwsgi /var/run/uwsgi \
    && chown appuser:appgroup /var/run/uwsgi \
    && mkdir /home/appuser/urbandata-test \
    && chown -R appuser:appgroup /home/appuser

WORKDIR /home/appuser/urbandata-test

COPY --chown=appuser:appgroup . ./

USER appuser

ENTRYPOINT [ "gunicorn", "-c", "./build/prod/gunicorn_conf.py", "config.wsgi:application" ]


# Service development image
FROM python:${PYTHON_VERSION} AS urbandata-test-dev


COPY --from=urbandata-python38-base /wheels /wheels

RUN set -x \
    && apk add --no-cache \
        libpq \
        mailcap \
    # Installing dependencies
    && pip install --upgrade pip \
    && pip install -r /wheels/requirements_dev.txt -f /wheels \
    # Cleaning up image
    && rm -rf /wheels \
    && rm -rf /root/.cache

WORKDIR /opt/urbandata-test

COPY . ./

CMD [ "gunicorn", "-c", "./build/dev/gunicorn_conf.py", "config.wsgi:application" ]
