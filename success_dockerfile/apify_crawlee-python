FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/apify/crawlee-python.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /crawlee-python/. /repo && rm -rf /crawlee-python/ && \
    rm -rf /crawlee-python && \
    cd /repo && git checkout 26706353843d0db739bc1045963a3e425c2168e5 && \
    cd /repo && poetry install && \
    cd /repo && poetry add playwright curl-cffi parsel && \
    cd /repo && poetry install --extras "all"