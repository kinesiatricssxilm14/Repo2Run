FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ShoggothAI/motleycrew.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /motleycrew/. /repo && rm -rf /motleycrew/ && \
    rm -rf /motleycrew && \
    cd /repo && git checkout 19837e76c89f1e96707dbe2c334360682c47b890 && \
    cd /repo && poetry install && \
    pip install langchain_core==0.3.21 && \
    pip install langchain_community==0.3.9 && \
    pip install kuzu==0.7.0 && \
    pip install langchain_experimental==0.3.3 && \
    pip install langchain_openai==0.2.11 && \
    pip install llama_index==0.12.3