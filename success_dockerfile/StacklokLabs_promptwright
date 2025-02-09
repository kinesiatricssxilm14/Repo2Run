FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/StacklokLabs/promptwright.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /promptwright/. /repo && rm -rf /promptwright/ && \
    rm -rf /promptwright && \
    cd /repo && git checkout 42f69b0055f575bfacd245ccffe6030657141f58 && \
    cd /repo && poetry install && \
    pip install pytest==8.3.4 && \
    pip install pytest-xdist==3.6.1 && \
    pip install pydantic==2.10.3 && \
    pip install click==8.1.7 && \
    pip install pyyaml==6.0.2 && \
    pip install huggingface-hub==0.27.0 && \
    pip install litellm==1.55.3 && \
    pip install datasets==3.2.0