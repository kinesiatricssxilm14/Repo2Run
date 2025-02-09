FROM python:3.12
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/All-Hands-AI/OpenHands.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /OpenHands/. /repo && rm -rf /OpenHands/ && \
    rm -rf /OpenHands && \
    cd /repo && git checkout 246107c618833fcf62e44f2ea67aa08c222906cb && \
    cd /repo && poetry install && \
    mkdir -p /repo/evaluation/agenthub