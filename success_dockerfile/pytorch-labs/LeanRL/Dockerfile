FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/pytorch-labs/LeanRL.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /LeanRL/. /repo && rm -rf /LeanRL/ && \
    rm -rf /LeanRL && \
    cd /repo && git checkout a416e61058ffa2dfe571bfe1d69a7f62d622b503 && \
    pip install gymnasium==0.29.1 && \
    pip install matplotlib==3.10.0 && \
    pip install moviepy==2.1.1 && \
    pip install numpy==1.26.4 && \
    pip install pandas==2.2.3 && \
    pip install protobuf==5.29.1 && \
    pip install pygame==2.6.1 && \
    pip install stable-baselines3==2.4.0 && \
    pip install tqdm==4.67.1 && \
    pip install wandb==0.19.1 && \
    pip install torchrl==0.6.0 && \
    pip install tensordict==0.6.2 && \
    pip install tyro==0.9.2