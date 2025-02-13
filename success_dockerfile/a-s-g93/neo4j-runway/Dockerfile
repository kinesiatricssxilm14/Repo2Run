FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/a-s-g93/neo4j-runway.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /neo4j-runway/. /repo && rm -rf /neo4j-runway/ && \
    rm -rf /neo4j-runway && \
    cd /repo && git checkout 16b44177d434465f7fbeef59273444c963343726 && \
    cd /repo && poetry install