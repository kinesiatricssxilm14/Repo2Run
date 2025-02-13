FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/xdit-project/xDiT.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /xDiT/. /repo && rm -rf /xDiT/ && \
    rm -rf /xDiT && \
    cd /repo && git checkout a7bd51915fc0b31dd0fdca30adab1fea8c2b7354 && \
    pip install torch==2.5.1 && \
    apt-get update -qq && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    cd /repo && pip install -e . && \
    apt-get update -qq && \
    apt-get update -qq && \
    apt-get install -y -qq gnupg2 curl && \
    curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | apt-key add - && \
    curl -s -L https://nvidia.github.io/nvidia-container-runtime/nvidia-container-runtime.list | tee /etc/apt/sources.list.d/nvidia-container-runtime.list && \
    apt-get update -qq && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    pip install yunchang==0.6.0 -U && \
    pip install yunchang==0.6.0 && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    pip install ninja==1.11.1.3
ENV CUDA_HOME=/usr/local/cuda-11
RUN apt-get update -qq && \
    apt-get update -qq && \
    apt-get install -y -qq gnupg2 curl && \
    curl -s -L https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin | tee /etc/apt/preferences.d/cuda-repository-pin-600 && \
    curl -s -L https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-ubuntu2004-11-8-local_11.8.0-500.101.06-1_amd64.deb -o /tmp/cuda-repo-ubuntu2004-11-8-local_11.8.0-500.101.06-1_amd64.deb && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub && \
    apt-get update -qq && \
    pip install diffusers==0.32.1 && \
    pip install distvae==0.0.0b4 && \
    pip install Flask==2.2.2 && \
    pip install huggingface_hub==0.27.0 && \
    pip install imageio==2.26.0 && \
    pip install numpy==1.23.5 && \
    pip install onediff==1.2.0 && \
    pip install optimum==1.23.3 && \
    pip install packaging==24.2 && \
    pip install Pillow==9.4.0 && \
    pip install pytest==7.1.2 && \
    pip install setuptools==65.6.3 && \
    pip install torch==2.5.1 && \
    pip install torch_xla==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install tqdm==4.67.1 && \
    pip install yunchang==0.6.0
ENV CUDA_HOME=/usr/local/cuda
RUN pip install nvidia-cudnn-cu11==9.6.0.74 nvidia-cusolver-cu11==11.4.1.48
ENV CUDA_HOME=/usr/local/
ENV CUDA_HOME=/usr/local/cuda-11/
RUN python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch"
RUN cd /repo && pytest --collect-only -q