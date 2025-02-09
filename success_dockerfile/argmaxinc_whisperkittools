FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/argmaxinc/whisperkittools.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /whisperkittools/. /repo && rm -rf /whisperkittools/ && \
    rm -rf /whisperkittools && \
    cd /repo && git checkout 03898fd293c694fc7a4c3c75d08b65d480ce2381 && \
    cd /repo && pip install -e . && \
    cd /repo && pip install -e .[android,evals]