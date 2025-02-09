FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/a-r-r-o-w/cogvideox-factory.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /cogvideox-factory/. /repo && rm -rf /cogvideox-factory/ && \
    rm -rf /cogvideox-factory && \
    cd /repo && git checkout 80d1150a0e233a1b2b98dd0367c06276989d049c && \
    pip install accelerate==1.2.1 && \
    pip install bitsandbytes==0.45.0 && \
    pip install diffusers==0.31.0 && \
    pip install transformers==4.47.1 && \
    pip install huggingface_hub==0.27.0 && \
    pip install hf_transfer==0.1.8 && \
    pip install peft==0.14.0 && \
    pip install decord==0.6.0 && \
    pip install wandb==0.19.1 && \
    pip install pandas==2.2.3 && \
    pip install torch==2.4.1 && \
    pip install torchvision==0.19.1 && \
    pip install torchao==0.7.0 && \
    pip install sentencepiece==0.2.0 && \
    pip install imageio-ffmpeg==0.5.1 && \
    pip install numpy==2.2.1