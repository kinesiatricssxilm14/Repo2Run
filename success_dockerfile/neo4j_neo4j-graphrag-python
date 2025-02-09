FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/neo4j/neo4j-graphrag-python.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /neo4j-graphrag-python/. /repo && rm -rf /neo4j-graphrag-python/ && \
    rm -rf /neo4j-graphrag-python && \
    cd /repo && git checkout bc6dd9c7b3f8fcfffb9ed360648ea80c6cbb17dc && \
    cd /repo && poetry install --with dev && \
    pip install fsspec==2024.10.0 && \
    pip install anthropic==0.40.0 && \
    pip install cohere==5.13.2 && \
    pip install mistralai==1.2.5 && \
    pip install openai==1.56.2 && \
    pip install weaviate==0.1.2 && \
    pip install pinecone-client==5.0.1 && \
    pip install qdrant-client==1.12.1 && \
    apt-get update -qq && \
    apt-get install graphviz -y -qq && \
    apt-get update -qq && \
    apt-get install graphviz-dev -y -qq && \
    cd /repo && poetry install --all-extras