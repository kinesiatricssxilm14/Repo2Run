FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/gpustack/gpustack.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /gpustack/. /repo && rm -rf /gpustack/ && \
    rm -rf /gpustack && \
    cd /repo && git checkout 3102d653f4829f6ce8468fb2d80eb54387dba26a && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q