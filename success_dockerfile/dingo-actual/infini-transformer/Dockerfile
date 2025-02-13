FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/dingo-actual/infini-transformer.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /infini-transformer/. /repo && rm -rf /infini-transformer/ && \
    rm -rf /infini-transformer && \
    cd /repo && git checkout 08d0a128710cd37da3e7be15f00ec683716aea0f && \
    pip install torch==2.5.1