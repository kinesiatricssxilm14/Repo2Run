FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/modelcontextprotocol/python-sdk.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /python-sdk/. /repo && rm -rf /python-sdk/ && \
    rm -rf /python-sdk && \
    cd /repo && git checkout aaf32b530738ff79ba607c2884374243350f521c && \
    pip install anyio==4.7.0 && \
    pip install httpx==0.28.1 && \
    pip install httpx-sse==0.4.0 && \
    pip install pydantic==2.10.4 && \
    pip install starlette==0.42.0 && \
    pip install sse-starlette==2.1.3 && \
    pip install pyright==1.1.391 && \
    pip install pytest==8.3.4 && \
    pip install ruff==0.8.4 && \
    pip install trio==0.27.0
ENV PYTHONPATH=/repo/src