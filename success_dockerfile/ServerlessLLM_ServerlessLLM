FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ServerlessLLM/ServerlessLLM.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ServerlessLLM/. /repo && rm -rf /ServerlessLLM/ && \
    rm -rf /ServerlessLLM && \
    cd /repo && git checkout 8f1e6b696e9bc2bdc6c4ca00752a0e4502746060 && \
    pip install fastapi==0.108.0 && \
    pip install GPUtil==1.4.0 && \
    pip install grpcio==1.49.1 && \
    pip install grpcio-tools==1.49.1 && \
    pip install openai==1.35.7 && \
    pip install pydantic==2.6.1 && \
    pip install pydantic_core==2.16.2 && \
    pip install ray==2.9.0 && \
    pip install requests==2.32.2 && \
    pip install serverless-llm-store==0.6.0 && \
    pip install speedtest-cli==2.1.3 && \
    pip install types-requests==2.31.0.20240125 && \
    pip install uvicorn[standard]==0.23.1 && \
    pip install accelerate==0.29.3 && \
    pip install outlines==0.0.43 && \
    pip install torch==2.3.0 && \
    pip install transformers==4.42.0 && \
    pip install vllm==0.5.0.post1