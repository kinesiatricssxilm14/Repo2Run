FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jahwag/ClaudeSync.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ClaudeSync/. /repo && rm -rf /ClaudeSync/ && \
    rm -rf /ClaudeSync && \
    cd /repo && git checkout 0006331542ed35956bfb80c50bd6f3b141348d9a && \
    pip install -r /repo/requirements.txt
ENV PYTHONPATH=/repo/src