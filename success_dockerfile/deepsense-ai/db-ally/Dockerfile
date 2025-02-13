FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/deepsense-ai/db-ally.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /db-ally/. /repo && rm -rf /db-ally/ && \
    rm -rf /db-ally && \
    cd /repo && git checkout 26033f72ab217e7ea20306081453b3414f841189 && \
    cd /repo && pip install -e . && \
    pip install pre-commit==4.0.1 && \
    pip install pytest==8.3.4 && \
    pip install pytest-asyncio==0.25.0 && \
    pip install pytest-cov==6.0.0 && \
    pip install pip-licenses==4.5.1 && \
    pip install bump2version==1.0.1 && \
    pip install mypy==1.8.0 && \
    pip install griffe==0.44.0 && \
    pip install griffe-typingdoc==0.2.5 && \
    pip install mkdocs==1.5.3 && \
    pip install mkdocs-autorefs==1.0.1 && \
    pip install mkdocs-material==9.5.13 && \
    pip install mkdocs-material-extensions==1.3.1 && \
    pip install mkdocstrings==0.24.1 && \
    pip install mkdocstrings-python==1.8.0 && \
    pip install litellm==1.55.3 && \
    pip install faiss-cpu==1.9.0.post1 && \
    pip install tenacity==9.0.0 && \
    pip install numpy==2.2.0 -U && \
    pip install pandas==2.2.3 -U --force-reinstall && \
    pip install chromadb==0.5.23 && \
    pip install rich==13.9.4
RUN cd /repo && pytest --collect-only -q