FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/run-llama/llama_deploy.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llama_deploy/. /repo && rm -rf /llama_deploy/ && \
    rm -rf /llama_deploy && \
    cd /repo && git checkout 47efff882cffa9b662f5a78e3032f5a13ea7bc17 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q