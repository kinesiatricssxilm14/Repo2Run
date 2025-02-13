FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/felafax/felafax.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /felafax/. /repo && rm -rf /felafax/ && \
    rm -rf /felafax && \
    cd /repo && git checkout 34a4758ad2329f97ebc6d4e60cd7b85be7b98e34 && \
    cd /repo && poetry install
ENV PYTHONPATH=/repo
RUN cd /repo && poetry run pytest --collect-only -q