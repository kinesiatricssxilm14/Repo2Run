FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/OpenInterpreter/aifs.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /aifs/. /repo && rm -rf /aifs/ && \
    rm -rf /aifs && \
    cd /repo && git checkout 3f74c6aaf6b1a190d99e7ab16d78163afbf1b1ca && \
    cd /repo && poetry install