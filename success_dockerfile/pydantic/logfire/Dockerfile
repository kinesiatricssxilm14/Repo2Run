FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/pydantic/logfire.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /logfire/. /repo && rm -rf /logfire/ && \
    rm -rf /logfire && \
    cd /repo && git checkout 3d79243b67ceb0b0adbdd1866609fb430947b8ba && \
    pip install aiohttp==3.11.10 && \
    pip install anyio==3.5.0 && \
    pip install attrs==22.1.0 && \
    pip install cloudpickle==2.0.0 && \
    pip install dirty_equals==0.8.0 && \
    pip install executing==2.1.0 && \
    pip install flask_sqlalchemy==3.1.1 && \
    pip install importlib_metadata==8.5.0 && \
    pip install inline_snapshot==0.17.0 && \
    pip install mkdocs==1.6.1 && \
    pip install numpy==1.23.5 && \
    pip install packaging==24.2 && \
    pip install pandas==1.5.3 && \
    pip install protobuf==5.29.1 && \
    pip install psutil==5.9.0 && \
    pip install psycopg2==2.9.10 && \
    pip install pyarrow==18.1.0 && \
    pip install pydantic_core==2.27.1 && \
    pip install pytest==7.1.2 && \
    pip install requests_mock==1.12.1 && \
    pip install rich==13.9.4 && \
    pip install setuptools==65.6.3 && \
    pip install sqlmodel==0.0.22 && \
    pip install testcontainers==4.9.0 && \
    pip install tomli==2.2.1 && \
    pip install typing_extensions==4.12.2 && \
    pip install Werkzeug==2.2.2 && \
    pip install opentelemetry-sdk==1.29.0 && \
    pip install opentelemetry-exporter-otlp-proto-http==1.29.0 && \
    pip install opentelemetry-instrumentation==0.50b0 && \
    pip install -e /repo && \
    pip install pytest-django==4.9.0 && \
    pip install django==5.1.4 && \
    pip install opentelemetry-instrumentation-redis==0.50b0 && \
    pip install opentelemetry-instrumentation-requests==0.50b0 && \
    pip install opentelemetry-instrumentation-sqlalchemy==0.50b0 && \
    pip install opentelemetry-instrumentation-sqlite3==0.50b0 && \
    pip install opentelemetry-instrumentation-starlette==0.50b0 && \
    pip install opentelemetry-instrumentation-system-metrics==0.50b0 && \
    pip install pymongo==4.10.1 && \
    pip install psycopg==3.2.3 && \
    pip install mysql==0.0.3 && \
    pip install httpx==0.28.1 && \
    pip install opentelemetry-instrumentation-psycopg==0.50b0 && \
    pip install opentelemetry-instrumentation-pymongo==0.50b0 && \
    pip install starlette==0.41.3 && \
    pip install fastapi==0.115.6 && \
    pip install opentelemetry-instrumentation-flask==0.50b0 && \
    pip install opentelemetry-instrumentation-httpx==0.50b0 && \
    pip install openai==1.57.4 && \
    pip install redis==5.2.1 && \
    pip install anthropic==0.40.0 && \
    pip install asyncpg==0.30.0 && \
    pip install opentelemetry-instrumentation-aiohttp-client==0.50b0 && \
    pip install opentelemetry-instrumentation-aws_lambda==0.50b0 && \
    pip install celery==5.4.0 && \
    pip install opentelemetry-instrumentation-django==0.50b0 && \
    pip install opentelemetry-instrumentation-fastapi==0.50b0 && \
    pip install loguru==0.7.3 && \
    pip install structlog==24.4.0 && \
    pip install opentelemetry-instrumentation-asyncpg==0.50b0 && \
    pip install opentelemetry-instrumentation-celery==0.50b0 && \
    pip install opentelemetry-instrumentation-psycopg2==0.50b0 && \
    pip install mysql-connector-python==9.1.0 pytest-vcr==1.0.2 && \
    pip install opentelemetry-instrumentation-mysql==0.50b0