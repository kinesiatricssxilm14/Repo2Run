FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Azure-Samples/rag-postgres-openai-python.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /rag-postgres-openai-python/. /repo && rm -rf /rag-postgres-openai-python/ && \
    rm -rf /rag-postgres-openai-python && \
    cd /repo && git checkout 61bde71a40ae76baa1445129a709d972f126f205 && \
    pip install ruff==0.8.3 && \
    pip install mypy==1.13.0 && \
    pip install types-requests==2.32.0.20241016 && \
    pip install pre-commit==4.0.1 && \
    pip install pip-tools==7.4.1 && \
    pip install pip-compile-cross-platform==1.4.2 && \
    pip install playwright==1.49.1 && \
    pip install pytest==8.3.4 && \
    pip install pytest-asyncio==0.25.0 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-playwright==0.6.2 && \
    pip install pytest-snapshot==0.9.0 && \
    pip install locust==2.32.4 && \
    pip install psycopg2==2.9.10 && \
    pip install dotenv-azd==0.2.0 && \
    pip install aiohappyeyeballs==2.4.4 && \
    pip install aiohttp==3.11.9 && \
    pip install aiosignal==1.3.1 && \
    pip install annotated-types==0.7.0 && \
    pip install anyio==4.6.2.post1 && \
    pip install asgiref==3.8.1 && \
    pip install async-timeout==5.0.1 && \
    pip install asyncpg==0.30.0 && \
    pip install attrs==24.2.0 && \
    pip install azure-core==1.32.0 && \
    pip install azure-core-tracing-opentelemetry==1.0.0b11 && \
    pip install azure-identity==1.19.0 && \
    pip install azure-monitor-opentelemetry==1.6.3 && \
    pip install azure-monitor-opentelemetry-exporter==1.0.0b32 && \
    pip install certifi==2024.8.30 && \
    pip install cffi==1.17.1 && \
    pip install charset-normalizer==3.4.0 && \
    pip install click==8.1.7 && \
    pip install cryptography==44.0.0 && \
    pip install deprecated==1.2.15 && \
    pip install distro==1.9.0 && \
    pip install environs==11.2.1 && \
    pip install exceptiongroup==1.2.2 && \
    pip install fastapi==0.115.5 && \
    pip install fixedint==0.1.6 && \
    pip install frozenlist==1.5.0 && \
    pip install greenlet==3.1.1 && \
    pip install h11==0.14.0 && \
    pip install httpcore==1.0.7 && \
    pip install httpx==0.28.0 && \
    pip install idna==3.10 && \
    pip install importlib-metadata==8.4.0 && \
    pip install isodate==0.7.2 && \
    pip install jiter==0.8.0 && \
    pip install marshmallow==3.23.1 && \
    pip install msal==1.31.1 && \
    pip install msal-extensions==1.2.0 && \
    pip install msrest==0.7.1 && \
    pip install multidict==6.1.0 && \
    pip install numpy==2.0.2 && \
    pip install oauthlib==3.2.2 && \
    pip install openai==1.55.3 && \
    pip install openai-messages-token-helper==0.1.10 && \
    pip install opentelemetry-api==1.27.0 && \
    pip install opentelemetry-instrumentation==0.48b0 && \
    pip install opentelemetry-instrumentation-aiohttp-client==0.48b0 && \
    pip install opentelemetry-instrumentation-asgi==0.48b0 && \
    pip install opentelemetry-instrumentation-dbapi==0.48b0 && \
    pip install opentelemetry-instrumentation-django==0.48b0 && \
    pip install opentelemetry-instrumentation-fastapi==0.48b0 && \
    pip install opentelemetry-instrumentation-flask==0.48b0 && \
    pip install opentelemetry-instrumentation-openai==0.33.9 && \
    pip install opentelemetry-instrumentation-psycopg2==0.48b0 && \
    pip install opentelemetry-instrumentation-requests==0.48b0 && \
    pip install opentelemetry-instrumentation-sqlalchemy==0.48b0 && \
    pip install opentelemetry-instrumentation-urllib==0.48b0 && \
    pip install opentelemetry-instrumentation-urllib3==0.48b0 && \
    pip install opentelemetry-instrumentation-wsgi==0.48b0 && \
    pip install opentelemetry-resource-detector-azure==0.1.5 && \
    pip install opentelemetry-sdk==1.27.0 && \
    pip install opentelemetry-semantic-conventions==0.48b0 && \
    pip install opentelemetry-semantic-conventions-ai==0.4.2 && \
    pip install opentelemetry-util-http==0.48b0 && \
    pip install packaging==24.2 && \
    pip install pgvector==0.3.6 && \
    pip install pillow==11.0.0 && \
    pip install portalocker==2.10.1 && \
    pip install propcache==0.2.1 && \
    pip install psutil==5.9.8 && \
    pip install pycparser==2.22 && \
    pip install pydantic==2.10.2 && \
    pip install pydantic-core==2.27.1 && \
    pip install pyjwt==2.10.1 && \
    pip install python-dotenv==1.0.1 && \
    pip install regex==2024.11.6 && \
    pip install requests==2.32.3 && \
    pip install requests-oauthlib==2.0.0 && \
    pip install setuptools==75.6.0 && \
    pip install six==1.16.0 && \
    pip install sniffio==1.3.1 && \
    pip install sqlalchemy==2.0.36 && \
    pip install starlette==0.41.3 && \
    pip install tiktoken==0.7.0 && \
    pip install tqdm==4.67.1 && \
    pip install typing-extensions==4.12.2 && \
    pip install urllib3==2.2.3 && \
    pip install uvicorn==0.32.1 && \
    pip install wrapt==1.17.0 && \
    pip install yarl==1.18.3 && \
    pip install zipp==3.21.0