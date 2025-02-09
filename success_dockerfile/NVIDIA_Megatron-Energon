FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/NVIDIA/Megatron-Energon.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Megatron-Energon/. /repo && rm -rf /Megatron-Energon/ && \
    rm -rf /Megatron-Energon && \
    cd /repo && git checkout 28aa3b79f4746968c76bc2e75c8a828c73e062c5 && \
    pip install braceexpand==0.1.7 click==8.1.7 numpy==2.2.0 pillow==11.0.0 pyyaml==6.0.2 torch==2.5.1 tqdm==4.67.1 webdataset==0.2.100 s3fs==2024.10.0 black==24.10.0 isort==5.13.2 sphinxcontrib-napoleon==0.7 sphinx==8.1.3 myst-parser==4.0.0 sphinx-rtd-theme==3.0.2 sphinx-click==6.0.0 torchvision==0.20.1
ENV PYTHONPATH=/repo/src