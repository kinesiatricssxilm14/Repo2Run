FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/volfpeter/htmy.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /htmy/. /repo && rm -rf /htmy/ && \
    rm -rf /htmy && \
    cd /repo && git checkout 0322a3996e87e8f3a29eca7d48099c069562c0d4 && \
    cd /repo && poetry install && \
    pip list | grep pytest && \
    pip install pytest-random-order==1.1.1 && \
    pip install anyio==4.7.0 && \
    pip install async-lru==2.0.4 && \
    pip install markdown==3.7