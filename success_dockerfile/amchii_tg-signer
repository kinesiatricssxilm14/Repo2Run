FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/amchii/tg-signer.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /tg-signer/. /repo && rm -rf /tg-signer/ && \
    rm -rf /tg-signer && \
    cd /repo && git checkout 926dbb8d58a40a44e75e5f0543fef68c4b833b44 && \
    pip install kurirogram==2.1.34 && \
    pip install click==8.1.7 && \
    pip install pydantic==2.10.4 && \
    pip install tgcrypto==1.2.5 && \
    pip install pytest==8.3.4
RUN cd /repo && pytest --collect-only -q