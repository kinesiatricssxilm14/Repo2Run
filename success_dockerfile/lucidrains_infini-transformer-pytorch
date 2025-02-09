FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lucidrains/infini-transformer-pytorch.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /infini-transformer-pytorch/. /repo && rm -rf /infini-transformer-pytorch/ && \
    rm -rf /infini-transformer-pytorch && \
    cd /repo && git checkout 5774bb32033c6794c8ced1905fa9d0c8a1adb025 && \
    pip install einops==0.8.0 && \
    pip install rotary-embedding-torch==0.8.6 && \
    pip install torch==2.5.1 && \
    pip install tqdm==4.67.1 && \
    pip install ruff==0.8.3 && \
    pip install pytest==8.3.4