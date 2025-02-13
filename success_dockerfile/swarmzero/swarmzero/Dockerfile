FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/swarmzero/swarmzero.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /swarmzero/. /repo && rm -rf /swarmzero/ && \
    rm -rf /swarmzero && \
    cd /repo && git checkout 6fcd7ac491aa76a8455e9079e7b012ba6a001fa6 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q