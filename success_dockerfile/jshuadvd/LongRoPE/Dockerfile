FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jshuadvd/LongRoPE.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /LongRoPE/. /repo && rm -rf /LongRoPE/ && \
    rm -rf /LongRoPE && \
    cd /repo && git checkout eb9abaaf5fe57eb94025d568d63d3c49d9cba746 && \
    cd /repo && poetry install && \
    pip install torch==2.2.1 && \
    pip install transformers==4.39.3 && \
    pip install datasets==2.20.0 && \
    pip install accelerate==0.31.0 && \
    pip install wandb==0.17.4 && \
    pip install gputil==1.4.0