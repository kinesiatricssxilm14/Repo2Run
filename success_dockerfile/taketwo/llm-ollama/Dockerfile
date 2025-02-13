FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/taketwo/llm-ollama.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llm-ollama/. /repo && rm -rf /llm-ollama/ && \
    rm -rf /llm-ollama && \
    cd /repo && git checkout dd616e755568e70457943c069ef197becd914cd9 && \
    pip install llm==0.19.1 && \
    pip install ollama==0.4.4 && \
    pip install pydantic==2.10.3 && \
    pip install pytest==8.3.4 && \
    pip install pytest-asyncio==0.25.0 && \
    pip install black==24.10.0
ENV PYTHONPATH=/repo