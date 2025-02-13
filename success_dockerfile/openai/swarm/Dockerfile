FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/openai/swarm.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /swarm/. /repo && rm -rf /swarm/ && \
    rm -rf /swarm && \
    cd /repo && git checkout 9db581cecaacea0d46a933d6453c312b034dbf47 && \
    cd /repo && pip install -e .