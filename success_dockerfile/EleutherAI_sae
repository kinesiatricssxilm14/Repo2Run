FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/EleutherAI/sae.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /sae/. /repo && rm -rf /sae/ && \
    rm -rf /sae && \
    cd /repo && git checkout 0483b52e0e2bf17daa1bf27da19f6482f47a7823 && \
    pip install accelerate==1.2.1 && \
    pip install datasets==3.2.0 && \
    pip install einops==0.8.0 && \
    pip install huggingface-hub==0.27.0 && \
    pip install natsort==8.4.0 && \
    pip install safetensors==0.4.5 && \
    pip install simple-parsing==0.1.6 && \
    pip install torch==2.5.1 && \
    pip install transformers==4.47.0