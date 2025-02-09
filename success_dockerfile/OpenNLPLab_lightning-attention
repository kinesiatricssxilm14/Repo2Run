FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/OpenNLPLab/lightning-attention.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /lightning-attention/. /repo && rm -rf /lightning-attention/ && \
    rm -rf /lightning-attention && \
    cd /repo && git checkout d7439519541e966084eeaaf3ffd63eecc216f414 && \
    cd /repo && pip install -e .
RUN cd /repo && pytest --collect-only -q