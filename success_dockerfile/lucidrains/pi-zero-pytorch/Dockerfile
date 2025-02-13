FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lucidrains/pi-zero-pytorch.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /pi-zero-pytorch/. /repo && rm -rf /pi-zero-pytorch/ && \
    rm -rf /pi-zero-pytorch && \
    cd /repo && git checkout 6716ce2f79c6eaad5f863b271f7d5ba3068af9d6 && \
    pip install beartype==0.19.0 && \
    pip install einx==0.3.0 && \
    pip install einops==0.8.0 && \
    pip install ema-pytorch==0.7.7 && \
    pip install jaxtyping==0.2.36 && \
    pip install rotary-embedding-torch==0.8.6 && \
    pip install scipy==1.14.1 && \
    pip install torch==2.5.1 && \
    pip install torchdiffeq==0.2.5 && \
    pip install torchtyping==0.1.5 && \
    pip install tqdm==4.67.1 && \
    pip install pytest==8.3.3 && \
    pip install ruff==0.8.2 && \
    pip install vit-pytorch==1.8.9