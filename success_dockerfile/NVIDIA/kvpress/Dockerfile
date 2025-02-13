FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/NVIDIA/kvpress.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /kvpress/. /repo && rm -rf /kvpress/ && \
    rm -rf /kvpress && \
    cd /repo && git checkout 715f8a7aae07a57b430aae8f869ac5a4c5bc48dd && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q