FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/martius-lab/hitchhiking-rotations.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /hitchhiking-rotations/. /repo && rm -rf /hitchhiking-rotations/ && \
    rm -rf /hitchhiking-rotations && \
    cd /repo && git checkout 45b49f68dd900b9c9bbc5ba98a14519c7f571484 && \
    cd /repo && pip install -e . && \
    pip install torch==2.5.1