FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/pomonam/kronfluence.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /kronfluence/. /repo && rm -rf /kronfluence/ && \
    rm -rf /kronfluence && \
    cd /repo && git checkout 884255f359e9b7d3d127f94c076901a838d63b09 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install accelerate==1.2.1 && \
    pip install einops==0.8.0 && \
    pip install einconv==0.1.0 && \
    pip install opt_einsum==3.4.0 && \
    pip install safetensors==0.4.5 && \
    pip install tqdm==4.67.1 && \
    pip install scikit-learn==1.6.0 && \
    pip install datasets==3.2.0 && \
    pip install transformers==4.47.1 && \
    pip install isort==5.13.2 && \
    pip install pylint==3.2.3 && \
    pip install pytest==8.2.2 && \
    pip install ruff==0.4.0
ENV LOCAL_RANK=0
ENV RANK=0
ENV LOCAL_RANK=0
ENV RANK=0
ENV LOCAL_RANK=0
ENV RANK=0
ENV WORLD_SIZE=1
RUN cd /repo && pytest --collect-only -q