FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/run-llama/llama_extract.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llama_extract/. /repo && rm -rf /llama_extract/ && \
    rm -rf /llama_extract && \
    cd /repo && git checkout 89438fafbfc89288a1e2d21cefd854b5066484f2 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q