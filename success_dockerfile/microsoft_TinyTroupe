FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/microsoft/TinyTroupe.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /TinyTroupe/. /repo && rm -rf /TinyTroupe/ && \
    rm -rf /TinyTroupe && \
    cd /repo && git checkout 9b8d4e9e02bfd98ece7cee2eddaf1bc5440c8c3e && \
    pip install pandas==2.2.3 && \
    pip install pytest==8.3.4 && \
    pip install openai==1.58.1 && \
    pip install tiktoken==0.8.0 && \
    pip install msal==1.31.1 && \
    pip install rich==13.9.4 && \
    pip install requests==2.32.3 && \
    pip install chevron==0.14.0 && \
    pip install llama-index==0.12.6 && \
    pip install llama-index-embeddings-huggingface==0.4.0 && \
    pip install llama-index-readers-web==0.3.1 && \
    pip install pypandoc==1.14 && \
    pip install docx==0.2.4 && \
    pip install markdown==3.7 && \
    pip install jupyter==1.1.1 && \
    pip install pydantic==2.10.3 && \
    cd /repo && pip install -e . && \
    ln -s /repo/examples /examples
RUN cd /repo && pytest --collect-only -q