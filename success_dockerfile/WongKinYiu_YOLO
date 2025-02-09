FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/WongKinYiu/YOLO.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /YOLO/. /repo && rm -rf /YOLO/ && \
    rm -rf /YOLO && \
    cd /repo && git checkout b96c8eaec16cfcabbf79947d98d2c575f0a114ad && \
    pip install einops==0.8.0 && \
    pip install graphviz==0.20.3 && \
    pip install hydra-core==1.3.2 && \
    pip install lightning==2.4.0 && \
    pip install loguru==0.7.3 && \
    pip install numpy==2.2.0 && \
    pip install opencv-python==4.10.0.84 && \
    pip install Pillow==11.0.0 && \
    pip install pycocotools==2.0.8 && \
    pip install requests==2.32.3 && \
    pip install rich==13.9.4 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install wandb==0.19.1 && \
    pip install gradio==5.9.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install pre-commit==4.0.1 && \
    pip install tensorboard==2.18.0
RUN cd /repo && pytest --collect-only -q