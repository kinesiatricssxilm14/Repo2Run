FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/line/lighthouse.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /lighthouse/. /repo && rm -rf /lighthouse/ && \
    rm -rf /lighthouse && \
    cd /repo && git checkout ba9da7228c2221f3c14ce3bbec0aa70bfd12d31c && \
    cd /repo && pip install -e . && \
    pip install torchtext==0.16.0 && \
    pip show torch torchtext && \
    pip install torchtext==0.16.0