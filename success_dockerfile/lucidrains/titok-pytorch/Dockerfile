FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lucidrains/titok-pytorch.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /titok-pytorch/. /repo && rm -rf /titok-pytorch/ && \
    rm -rf /titok-pytorch && \
    cd /repo && git checkout 2f95258f27797f142df0d5dc2388e034285ab7e5 && \
    pip install titok-pytorch==0.0.5