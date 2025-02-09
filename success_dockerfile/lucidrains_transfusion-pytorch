FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lucidrains/transfusion-pytorch.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /transfusion-pytorch/. /repo && rm -rf /transfusion-pytorch/ && \
    rm -rf /transfusion-pytorch && \
    cd /repo && git checkout 16f73e17aa5deeec044f3bdc1f7d3686528da4d2 && \
    pip install hatch==1.14.0 && \
    cd /repo && hatch build && \
    cd /repo && hatch env create && \
    pip install torch==2.5.1 && \
    pip install einops==0.8.0 && \
    pip install torchdiffeq==0.2.5 && \
    pip install einx==0.3.0 && \
    pip install ema_pytorch==0.7.7 && \
    pip install rotary_embedding_torch==0.8.6 && \
    pip install tqdm==4.67.1 && \
    pip install loguru==0.7.3 && \
    pip install jaxtyping==0.2.36 && \
    pip install beartype==0.19.0