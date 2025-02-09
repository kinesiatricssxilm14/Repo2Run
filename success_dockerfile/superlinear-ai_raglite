FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/superlinear-ai/raglite.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /raglite/. /repo && rm -rf /raglite/ && \
    rm -rf /raglite && \
    cd /repo && git checkout 0c5b7b56dbe48781e51857366ed9c3f82604d7c0 && \
    cd /repo && poetry install