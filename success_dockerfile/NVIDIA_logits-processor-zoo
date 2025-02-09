FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/NVIDIA/logits-processor-zoo.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /logits-processor-zoo/. /repo && rm -rf /logits-processor-zoo/ && \
    rm -rf /logits-processor-zoo && \
    cd /repo && git checkout db179ad1035b37d98b8b3edae6e27aea2c05bfb0 && \
    pip install torch==2.3.0 && \
    pip install transformers==4.41.2 && \
    pip install accelerate==0.26.1 && \
    pip freeze && \
    cd /repo && pip install -e .