FROM python:3.12
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/daya0576/beaverhabits.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /beaverhabits/. /repo && rm -rf /beaverhabits/ && \
    rm -rf /beaverhabits && \
    cd /repo && git checkout c012577267047527362cfc0c9cfc17003b9212af && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q