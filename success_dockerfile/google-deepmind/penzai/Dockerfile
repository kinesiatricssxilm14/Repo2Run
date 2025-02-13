FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/google-deepmind/penzai.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /penzai/. /repo && rm -rf /penzai/ && \
    rm -rf /penzai && \
    cd /repo && git checkout fda6cd1e6883348ce7ff705d78149bc19631e93a && \
    pip install flit==3.10.1
ENV FLIT_ROOT_INSTALL=1
RUN cd /repo && flit install --symlink