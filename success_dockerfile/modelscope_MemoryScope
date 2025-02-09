FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/modelscope/MemoryScope.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /MemoryScope/. /repo && rm -rf /MemoryScope/ && \
    rm -rf /MemoryScope && \
    cd /repo && git checkout 330b7660c93f2ce9402946141192e91031b7aae0 && \
    pip install llama-index==0.10.45 && \
    pip install llama-index-embeddings-dashscope==0.3.0 && \
    pip install llama-index-llms-dashscope==0.3.0 && \
    pip install llama-index-postprocessor-dashscope-rerank-custom==0.1.0 && \
    pip install dashscope==1.20.14 && \
    pip install llama-index-vector-stores-elasticsearch==0.4.0 && \
    pip install elasticsearch==8.17.0 && \
    pip install pyfiglet==1.0.2 && \
    pip install termcolor==2.5.0 && \
    pip install fire==0.7.0 && \
    pip install questionary==2.0.1 && \
    pip install pydantic==2.10.3 && \
    pip install pyyaml==6.0.2 && \
    pip install numpy==1.26.4 && \
    pip install rich==13.9.4