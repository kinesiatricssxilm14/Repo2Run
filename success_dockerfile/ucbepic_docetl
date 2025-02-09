FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ucbepic/docetl.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /docetl/. /repo && rm -rf /docetl/ && \
    rm -rf /docetl && \
    cd /repo && git checkout 8b3e1ce640d3ead04931d322cff4ea1047d3f860 && \
    cd /repo && poetry install