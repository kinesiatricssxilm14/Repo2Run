FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/mistralai/mistral-finetune.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mistral-finetune/. /repo && rm -rf /mistral-finetune/ && \
    rm -rf /mistral-finetune && \
    cd /repo && git checkout 656df1c94c80ca9703ebc471c9f106c9b7a0bfa7 && \
    pip install fire==0.7.0 && \
    pip install simple-parsing==0.1.6 && \
    pip install pyyaml==6.0.2 && \
    pip install mistral-common==1.5.1 && \
    pip install safetensors==0.4.5 && \
    pip install tensorboard==2.18.0 && \
    pip install tqdm==4.67.1 && \
    pip install torch==2.2.0 && \
    pip install triton==2.2.0 && \
    pip install xformers==0.0.24 && \
    pip install mypy==1.4.0 && \
    pip install mypy-extensions==1.0.0 && \
    pip install pre-commit==4.0.1 && \
    pip install ruff==0.0.282 && \
    pip install pytest==8.3.4