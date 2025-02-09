FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/dbos-inc/dbos-transact-py.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /dbos-transact-py/. /repo && rm -rf /dbos-transact-py/ && \
    rm -rf /dbos-transact-py && \
    cd /repo && git checkout d6c6ac62b317f123e52bdc361aeffd73a6ac65cc && \
    pip install pdm==2.22.0 && \
    cd /repo && pdm install && \
    pip install sqlalchemy==2.0.36 && \
    pip install fastapi==0.115.6 && \
    pip install flask==3.1.0 && \
    pip install opentelemetry-api==1.29.0 && \
    pip install opentelemetry-sdk==1.29.0 && \
    pip install opentelemetry-exporter-otlp-proto-http==1.29.0 && \
    pip install pyyaml==6.0.2 && \
    pip install jsonschema==4.23.0 && \
    pip install jsonpickle==4.0.1 && \
    pip install psycopg[binary]==3.2.3 && \
    pip install alembic==1.14.0 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install pytz==2024.2 && \
    pip install pyjwt==2.10.1 && \
    pip install confluent_kafka==2.6.1