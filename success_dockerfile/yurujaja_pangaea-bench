FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/yurujaja/pangaea-bench.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /pangaea-bench/. /repo && rm -rf /pangaea-bench/ && \
    rm -rf /pangaea-bench && \
    cd /repo && git checkout e1d12ed1e0aac945f32c8bc78e99666869f277d4 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install geopandas==1.0.1 && \
    pip install rasterio==1.4.3 && \
    pip install pillow==11.0.0 && \
    pip install scikit-learn==1.6.0 && \
    pip install tensorboard==2.18.0 && \
    pip install tqdm==4.67.1 && \
    pip install tifffile==2024.12.12 && \
    pip install timm==1.0.12 && \
    pip install einops==0.8.0 && \
    pip install opencv-python==4.10.0.84 && \
    pip install rioxarray==0.18.1 && \
    pip install gdown==5.2.0 && \
    pip install ptflops==0.7.4 && \
    pip install google-cloud-storage==2.19.0 && \
    pip install omegaconf==2.3.0 && \
    pip install pyDataverse==0.3.4 && \
    pip install pytest==8.3.4 && \
    pip install yacs==0.1.8 && \
    pip install wandb==0.19.1 && \
    pip install hydra-core==1.3.2