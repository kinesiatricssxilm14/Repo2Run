FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/simonw/llm-jq.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llm-jq/. /repo && rm -rf /llm-jq/ && \
    rm -rf /llm-jq && \
    cd /repo && git checkout beaada20d11dfc34618394c633bfa128a7c00a94 && \
    pip install llm==0.19.1 && \
    pip install pytest==8.3.4