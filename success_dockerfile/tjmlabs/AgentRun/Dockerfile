FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/tjmlabs/AgentRun.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /AgentRun/. /repo && rm -rf /AgentRun/ && \
    rm -rf /AgentRun && \
    cd /repo && git checkout 1997dd71d5350dd1e0c993cdd7060b3b9b765a8d && \
    pip install docker==7.1.0 && \
    pip install restrictedpython==7.4 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-benchmark==5.1.0 && \
    pip install mypy==1.13.0 && \
    pip install mkdocs==1.6.1 && \
    pip install mkdocs-material==9.5.49 && \
    pip install mkdocstrings[python]==0.27.0 && \
    pip install mkdocs-jupyter==0.25.1
ENV PYTHONPATH="/repo"