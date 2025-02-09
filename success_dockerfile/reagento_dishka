FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/reagento/dishka.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /dishka/. /repo && rm -rf /dishka/ && \
    rm -rf /dishka && \
    cd /repo && git checkout e6d576017fdad07fa93cf863e4fdd2f48828a3c0 && \
    pip install ruff==0.6.0 && \
    pip install tox==4.23.2 && \
    pip install tox-uv==1.15.0 && \
    pip install mypy==1.12.0 && \
    pip install dishka==1.4.2 && \
    pip install pytest-asyncio==0.24.0 && \
    pip install fastapi==0.115.6 && \
    pip install asgi_lifespan==2.1.0 && \
    pip install httpx==0.28.0 && \
    pip install uvicorn==0.32.1
RUN cd /repo && pytest --collect-only -q