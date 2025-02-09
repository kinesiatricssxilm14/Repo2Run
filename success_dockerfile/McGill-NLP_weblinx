FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/McGill-NLP/weblinx.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /weblinx/. /repo && rm -rf /weblinx/ && \
    rm -rf /weblinx && \
    cd /repo && git checkout 6f2014f025de764deba3442a52db0dc43fb784d0 && \
    cd /repo && pip install -e . && \
    pip install lxml==5.3.0