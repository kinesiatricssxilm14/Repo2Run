FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/foundation-model-stack/fms-fsdp.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fms-fsdp/. /repo && rm -rf /fms-fsdp/ && \
    rm -rf /fms-fsdp && \
    cd /repo && git checkout 408c7516d69ea9b6bcd4c0f5efab26c0f64b3c2d && \
    pip install torch==2.5.1 && \
    pip install fire==0.5.0 && \
    pip install pyarrow==15.0.0 && \
    pip install transformers==4.40.2 && \
    pip install ibm-fms==0.0.8 && \
    pip install black==24.1.1 && \
    pip install mypy==1.8.0 && \
    pip install mypy-extensions==1.0.0 && \
    pip install pytest==8.1.1 && \
    pip install pyarrow-stubs==10.0.1.7 && \
    pip install types-requests==2.31.0.20240125 && \
    pip install types-setuptools==69.0.0.20240125 && \
    pip install wandb==0.16.4 && \
    pip install aim==3.19.1
ENV PYTHONPATH=/repo