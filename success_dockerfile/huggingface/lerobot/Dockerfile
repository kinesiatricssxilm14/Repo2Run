FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/huggingface/lerobot.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /lerobot/. /repo && rm -rf /lerobot/ && \
    rm -rf /lerobot && \
    cd /repo && git checkout 4c41f6fcc624e1e495daf1d319034148df3f6793 && \
    cd /repo && poetry install && \
    pip install pyserial==3.5 && \
    pip install hydra-core==1.3.2 && \
    pip install numpy==2.2.0 && \
    pip install torch==2.5.1 && \
    pip install datasets==3.2.0 && \
    pip install pillow==11.0.0 && \
    pip install einops==0.8.0 && \
    pip install jsonlines==4.0.0 && \
    pip install torchvision==0.20.1 && \
    pip install gymnasium==0.29.1 && \
    pip install safetensors==0.4.5 && \
    pip install rerun-sdk==0.21.0 && \
    pip install flask==3.1.0 && \
    pip install diffusers==0.31.0 && \
    pip install deepdiff==8.1.1 && \
    pip install termcolor==2.5.0 && \
    pip install opencv-python-headless==4.10.0.84 && \
    pip install imageio==2.36.1