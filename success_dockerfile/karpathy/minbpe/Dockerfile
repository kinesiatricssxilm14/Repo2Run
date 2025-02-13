FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/karpathy/minbpe.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /minbpe/. /repo && rm -rf /minbpe/ && \
    rm -rf /minbpe && \
    cd /repo && git checkout 1acefe89412b20245db5a22d2a02001e547dc602 && \
    pip install regex==2024.11.6 && \
    pip install tiktoken==0.8.0