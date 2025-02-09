FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/IvanDrokin/torch-conv-kan.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /torch-conv-kan/. /repo && rm -rf /torch-conv-kan/ && \
    rm -rf /torch-conv-kan && \
    cd /repo && git checkout 7a0e83c3b55981e530dc83ad44ecc4d24beb5d20 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install tqdm==4.67.1 && \
    pip install accelerate==1.2.1 && \
    pip install wandb==0.19.1 && \
    pip install scikit-learn==1.6.0 && \
    pip install omegaconf==2.3.0 && \
    pip install hydra-core==1.3.2 && \
    pip install datasets==3.2.0 && \
    pip install pillow==11.0.0 && \
    pip install torchinfo==1.8.0 && \
    pip install torchmetrics==1.6.0 && \
    pip install einops==0.8.0 && \
    pip install matplotlib==3.10.0 && \
    pip install huggingface_hub==0.27.0 && \
    pip install lion-pytorch==0.2.3 && \
    pip install imbalanced-learn==0.13.0 && \
    pip install albumentations==1.4.23 && \
    pip install ray[tune]==2.40.0 && \
    pip install medpy==0.5.2 && \
    pip install timm==1.0.12 && \
    pip install iterative-stratification==0.1.9