FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Genentech/gReLU.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /gReLU/. /repo && rm -rf /gReLU/ && \
    rm -rf /gReLU && \
    cd /repo && git checkout efd30819a894c10d7dfda2a111f85825240d52c9 && \
    pip install -e /repo && \
    pip install pytest-cov==6.0.0
RUN cd /repo && pytest --collect-only -q