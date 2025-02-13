FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/google-deepmind/nanodo.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /nanodo/. /repo && rm -rf /nanodo/ && \
    rm -rf /nanodo && \
    cd /repo && git checkout 10aefdeed40a63293daf112b91a5538cd24fa3a4 && \
    cd /repo && pip install flit==3.10.1
ENV FLIT_ROOT_INSTALL=1
RUN cd /repo && flit install