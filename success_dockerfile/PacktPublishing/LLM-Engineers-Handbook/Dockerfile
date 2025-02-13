FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/PacktPublishing/LLM-Engineers-Handbook.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /LLM-Engineers-Handbook/. /repo && rm -rf /LLM-Engineers-Handbook/ && \
    rm -rf /LLM-Engineers-Handbook && \
    cd /repo && git checkout ec6717fd3ef78c5b5f0efcfc207679436417bc0c && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q