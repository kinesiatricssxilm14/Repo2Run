FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ultrasev/llmproxy.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llmproxy/. /repo && rm -rf /llmproxy/ && \
    rm -rf /llmproxy && \
    cd /repo && git checkout 1a1100aa098220b1de5c9716a8ce3aa253716aee && \
    pip install fastapi==0.88.0 && \
    pip install pytest==7.1.3 && \
    pip install pytest-asyncio==0.20.3 && \
    pip install uvicorn==0.20.0 && \
    pip install pydantic==1.10.19 && \
    pip install python-multipart==0.0.5 && \
    pip install expiringdict==1.2.2 && \
    pip install rich==13.4.2 && \
    pip install openai==1.6.1 && \
    pip install httpx==0.27.0 && \
    pip install python-dotenv==1.0.1 && \
    pip install codefast==24.11.14.18 && \
    pip install aiohttp==3.11.9