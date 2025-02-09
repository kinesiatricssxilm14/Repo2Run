FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/remigenet/TKAN.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /TKAN/. /repo && rm -rf /TKAN/ && \
    rm -rf /TKAN && \
    cd /repo && git checkout 8a1de0cfda6f0bd90a91e6793255a29ca80f5134 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q