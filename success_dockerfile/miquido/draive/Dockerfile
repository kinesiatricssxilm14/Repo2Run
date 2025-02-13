FROM python:3.12
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/miquido/draive.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /draive/. /repo && rm -rf /draive/ && \
    rm -rf /draive && \
    cd /repo && git checkout 270f0ce1375dade2e9a54dfa4c48a7155e3bb310 && \
    pip install numpy==2.2.0 && \
    pip install haiway==0.5.3 && \
    pip install sentencepiece==0.2.0 && \
    pip install fastembed==0.4.2 && \
    pip install openai==1.57.4 && \
    pip install tiktoken==0.8.0 && \
    pip install anthropic==0.40.0 && \
    pip install tokenizers==0.21.0 && \
    pip install httpx==0.28.1 && \
    pip install boto3==1.35.82 && \
    pip install ruff==0.8.3 && \
    pip install pyright==1.1.390 && \
    pip install bandit==1.8.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-asyncio==0.25.0
ENV PYTHONPATH=/repo/src
RUN pip show haiway && \
    pip install haiway==0.5.3
ENV PYTHONPATH=/repo/src