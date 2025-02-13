FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jina-ai/late-chunking.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /late-chunking/. /repo && rm -rf /late-chunking/ && \
    rm -rf /late-chunking && \
    cd /repo && git checkout db558c313a63a6b6f575281be9a3a87ad0fc1d4b && \
    pip install jupyterlab==4.2.5 && \
    pip install transformers==4.43.4 && \
    pip install torch==2.4.0 && \
    pip install mteb==1.14.20 && \
    pip install datasets==2.19.1 && \
    pip install llama-index-embeddings-huggingface==0.3.1 && \
    pip install llama-index==0.11.10 && \
    pip install click==8.1.7 && \
    pip install einops==0.6.1