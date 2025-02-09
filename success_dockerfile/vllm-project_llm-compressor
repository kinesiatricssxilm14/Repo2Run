FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/vllm-project/llm-compressor.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llm-compressor/. /repo && rm -rf /llm-compressor/ && \
    rm -rf /llm-compressor && \
    cd /repo && git checkout 606aab2b57eb0931f93976f6011f2b2869ebdc60 && \
    cd /repo && pip install -e . && \
    cd /repo && pip install -e .[dev]