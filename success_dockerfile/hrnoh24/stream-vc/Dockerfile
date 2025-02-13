FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/hrnoh24/stream-vc.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /stream-vc/. /repo && rm -rf /stream-vc/ && \
    rm -rf /stream-vc && \
    cd /repo && git checkout faa629f54dfd518702fb0d78018340b87fdebbd1 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install lightning==2.4.0 && \
    pip install torchmetrics==1.6.0 && \
    pip install hydra-core==1.3.2 && \
    pip install rootutils==1.0.7 && \
    pip install pre-commit==4.0.1 && \
    pip install rich==13.9.4 && \
    pip install pytest==8.3.4 && \
    pip install einops==0.8.0 && \
    pip install vector-quantize-pytorch==1.20.11 && \
    pip install local-attention==1.9.15 && \
    pip install gateloop-transformer==0.2.5 && \
    pip install packaging==24.2 && \
    pip install tensorboardX==2.6.2.2 && \
    pip install requests==2.32.3 && \
    pip install librosa==0.10.2.post1 && \
    pip install matplotlib==3.10.0