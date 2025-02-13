FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/andrewyng/aisuite.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /aisuite/. /repo && rm -rf /aisuite/ && \
    rm -rf /aisuite && \
    cd /repo && git checkout 763996153e3c6068465bd73a367a20f6ca79cefc && \
    cd /repo && poetry install && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install vertexai==1.71.1 && \
    pip install groq==0.13.1 && \
    pip install mistralai==1.2.5 && \
    pip install httpx==0.27.2 && \
    pip install openai==1.57.4 && \
    pip install ibm-watsonx-ai==1.1.26