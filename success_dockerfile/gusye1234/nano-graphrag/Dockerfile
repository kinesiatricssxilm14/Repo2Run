FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/gusye1234/nano-graphrag.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /nano-graphrag/. /repo && rm -rf /nano-graphrag/ && \
    rm -rf /nano-graphrag && \
    cd /repo && git checkout 18fa3a4f23a1befb11f2d8f1d37df28671d6243e && \
    pip install future==1.0.0 && \
    pip install openai==1.58.1 && \
    pip install tiktoken==0.8.0 && \
    pip install networkx==3.4.2 && \
    pip install graspologic==3.4.1 && \
    pip install nano-vectordb==0.0.4.3 && \
    pip install hnswlib==0.8.0 && \
    pip install xxhash==3.5.0 && \
    pip install tenacity==9.0.0 && \
    pip install dspy-ai==2.5.43 && \
    pip install neo4j==5.27.0 && \
    pip install aioboto3==13.2.0
RUN cd /repo && pytest --collect-only -q