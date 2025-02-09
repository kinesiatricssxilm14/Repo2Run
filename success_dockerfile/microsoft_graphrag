FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/microsoft/graphrag.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /graphrag/. /repo && rm -rf /graphrag/ && \
    rm -rf /graphrag && \
    cd /repo && git checkout 5ff2d3c76d2d08797d3337bbe5278c165324f441 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q