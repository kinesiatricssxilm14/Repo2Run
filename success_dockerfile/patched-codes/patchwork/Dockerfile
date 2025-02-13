FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/patched-codes/patchwork.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /patchwork/. /repo && rm -rf /patchwork/ && \
    rm -rf /patchwork && \
    cd /repo && git checkout c9b02b065780cb9f4b6c16a2d86a2a328ffd0fc5 && \
    cd /repo && poetry install && \
    cd /repo && poetry install --extras "rag notifications"
RUN cd /repo && poetry run pytest --collect-only -q