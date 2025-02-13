FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/antgroup/agentUniverse.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /agentUniverse/. /repo && rm -rf /agentUniverse/ && \
    rm -rf /agentUniverse && \
    cd /repo && git checkout ed8f55b52b65f8da539f87593e5448258658038a && \
    cd /repo && poetry install && \
    cd /repo && poetry install -E log_ext -E store_ext
RUN cd /repo && poetry run pytest --collect-only -q