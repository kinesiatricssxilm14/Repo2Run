FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jmschrei/tangermeme.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /tangermeme/. /repo && rm -rf /tangermeme/ && \
    rm -rf /tangermeme && \
    cd /repo && git checkout a96897f3c78281d1f83ab0d4f3011af57aef4b32 && \
    cd /repo && pip install -e .
RUN cd /repo && pytest --collect-only -q