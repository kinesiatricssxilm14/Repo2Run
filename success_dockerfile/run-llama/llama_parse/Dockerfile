FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/run-llama/llama_parse.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llama_parse/. /repo && rm -rf /llama_parse/ && \
    rm -rf /llama_parse && \
    cd /repo && git checkout 483b51c51c0dcae16fc24dd5c852e94ad0533380 && \
    cd /repo && poetry install && \
    pip install fsspec==2024.10.0 && \
    pip install httpx==0.28.1 && \
    pip install llama_index==0.12.3
RUN cd /repo && pytest --collect-only -q