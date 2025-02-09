FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/getzep/graphiti.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /graphiti/. /repo && rm -rf /graphiti/ && \
    rm -rf /graphiti && \
    cd /repo && git checkout 9f3dd5552a611b7c329e3c1c7d1254102ad2e40a && \
    cd /repo && poetry install