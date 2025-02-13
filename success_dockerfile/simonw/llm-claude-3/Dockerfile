FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/simonw/llm-claude-3.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llm-claude-3/. /repo && rm -rf /llm-claude-3/ && \
    rm -rf /llm-claude-3 && \
    cd /repo && git checkout c62bf247fa964ff350badf5424743ddca7601d4a && \
    pip install llm==0.19.1 && \
    pip install anthropic==0.40.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-recording==0.13.2 && \
    pip install pytest-asyncio==0.25.0