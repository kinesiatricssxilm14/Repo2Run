FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/AnswerDotAI/rerankers.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /rerankers/. /repo && rm -rf /rerankers/ && \
    rm -rf /rerankers && \
    cd /repo && git checkout ecd1f62949ec8aaffedeaaa89928e702dce2d148 && \
    cd /repo && pip install -e . && \
    pip install torch==2.5.1 && \
    pip install transformers==4.47.0