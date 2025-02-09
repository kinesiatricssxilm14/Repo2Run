FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/IBM/terratorch.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /terratorch/. /repo && rm -rf /terratorch/ && \
    rm -rf /terratorch && \
    cd /repo && git checkout 16e5af99b4b8ddb830ef1c6c3184916d3a74d107 && \
    pip install torchgeo==0.6.0 && \
    pip install rioxarray==0.15.0 && \
    pip install albumentations==1.3.1 && \
    pip install rasterio==1.3.10 && \
    pip install torch==2.3.1 && \
    pip install torchvision==0.18.1 && \
    pip install torchmetrics==1.4.0 && \
    pip install geopandas==0.14.4 && \
    pip install lightly==1.4.25 && \
    pip install h5py==3.12.1 && \
    pip install mlflow==2.14.3 && \
    pip install lightning==2.4.0 && \
    pip install segmentation-models-pytorch==0.3.4 && \
    pip install mkdocs-material==9.4.14 && \
    pip install mkdocstrings[python]==0.27.0 && \
    pip install h5py==3.12.1 && \
    pip install jupyterlab==4.3.4 && \
    pip install coverage[toml]==7.6.9 && \
    pip install pytest-cov==4.1.0 && \
    pip install pytest==8.3.3