FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/bellingcat/ShadowFinder.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ShadowFinder/. /repo && rm -rf /ShadowFinder/ && \
    rm -rf /ShadowFinder && \
    cd /repo && git checkout 578d5ac6d14341d04be35fc3c3665dc9b5e7e665 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q