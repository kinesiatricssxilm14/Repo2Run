FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/awslabs/agent-evaluation.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /agent-evaluation/. /repo && rm -rf /agent-evaluation/ && \
    rm -rf /agent-evaluation && \
    cd /repo && git checkout 3df69508f44cd77a7714be1649fe3dfe0d000ae2 && \
    cd /repo && pip install -e .
ENV PYTHONPATH=/repo/src
ENV PYTHONPATH=/repo/src/agenteval
ENV PYTHONPATH=/repo:/repo/src
RUN cd /repo && pytest --collect-only -q