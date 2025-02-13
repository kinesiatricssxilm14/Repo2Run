FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/apple/ml-cross-entropy.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ml-cross-entropy/. /repo && rm -rf /ml-cross-entropy/ && \
    rm -rf /ml-cross-entropy && \
    cd /repo && git checkout 9c297c905f55b73594b5d650722d1e78183b77bd && \
    cd /repo && pip install -e .[dev]