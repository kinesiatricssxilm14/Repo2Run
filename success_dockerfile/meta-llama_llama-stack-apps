FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/meta-llama/llama-stack-apps.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llama-stack-apps/. /repo && rm -rf /llama-stack-apps/ && \
    rm -rf /llama-stack-apps && \
    cd /repo && git checkout f14a73c76a9e4de3f7fd5ae5d13c231bd70ec2ce && \
    pip install fire==0.7.0 && \
    pip install python-dotenv==1.0.1 && \
    pip install setuptools==65.5.1 && \
    pip install yfinance==0.2.50 && \
    pip install gradio==5.9.1 && \
    pip install llama-stack-client==0.0.63