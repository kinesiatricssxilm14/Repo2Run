FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/DS4SD/docling.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /docling/. /repo && rm -rf /docling/ && \
    rm -rf /docling && \
    cd /repo && git checkout aee9c0b324a07190ad03ad3a6266e76c465d4cdf && \
    cd /repo && poetry install