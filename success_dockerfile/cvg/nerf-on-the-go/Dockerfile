FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/cvg/nerf-on-the-go.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /nerf-on-the-go/. /repo && rm -rf /nerf-on-the-go/ && \
    rm -rf /nerf-on-the-go && \
    cd /repo && git checkout 3659e7c3b5e71fb07be89980b99ef72526fb7099 && \
    pip install numpy==2.0.2 && \
    pip install jax==0.4.38 && \
    pip install jaxlib==0.4.38 && \
    pip install opencv-python==4.10.0.84 && \
    pip install Pillow==11.0.0 && \
    pip install tensorboard==2.18.0 && \
    pip install tensorflow==2.18.0 && \
    pip install gin-config==0.5.0 && \
    pip install dm_pix==0.4.3 && \
    pip install rawpy==0.24.0 && \
    pip install mediapy==1.2.2 && \
    pip install lpips_jax==0.1.0 && \
    pip install chex==0.1.88 && \
    pip install optax==0.2.4 && \
    pip install ml-dtypes==0.4.1 && \
    pip install flax==0.10.2 && \
    pip install gdown==5.2.0 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install torchaudio==2.5.1 && \
    pip install orbax-checkpoint==0.3.5 && \
    pip install matplotlib==3.8.4
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q