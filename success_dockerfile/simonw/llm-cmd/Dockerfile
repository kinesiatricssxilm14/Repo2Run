FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/simonw/llm-cmd.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llm-cmd/. /repo && rm -rf /llm-cmd/ && \
    rm -rf /llm-cmd && \
    cd /repo && git checkout 74fb986ee939808362e7a73a71b2e0edadded1bc && \
    pip install llm==0.19.1 && \
    pip install prompt_toolkit==3.0.48 && \
    pip install pygments==2.18.0 && \
    pip install pytest==8.3.4