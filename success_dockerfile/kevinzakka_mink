FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/kevinzakka/mink.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mink/. /repo && rm -rf /mink/ && \
    rm -rf /mink && \
    cd /repo && git checkout cf1a302ff31b1f620abecdcbdebfd2c42d125a54 && \
    cd /repo && pip install flit==3.10.1
ENV FLIT_ROOT_INSTALL=1
RUN cd /repo && flit install --deps all