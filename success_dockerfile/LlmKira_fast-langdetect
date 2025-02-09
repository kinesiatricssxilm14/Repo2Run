FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/LlmKira/fast-langdetect.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fast-langdetect/. /repo && rm -rf /fast-langdetect/ && \
    rm -rf /fast-langdetect && \
    cd /repo && git checkout 5728ba917383c45a08c8ac1cdab255c7c546435c && \
    pip install pdm==2.22.1 && \
    cd /repo && pdm install
RUN cd /repo && pytest --collect-only -q