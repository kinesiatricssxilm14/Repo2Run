FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/royreznik/rexi.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /rexi/. /repo && rm -rf /rexi/ && \
    rm -rf /rexi && \
    cd /repo && git checkout f1dca8eaa984a27a4a81a78cffb76e1d3b9ba467 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q