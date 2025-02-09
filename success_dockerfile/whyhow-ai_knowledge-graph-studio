FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/whyhow-ai/knowledge-graph-studio.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /knowledge-graph-studio/. /repo && rm -rf /knowledge-graph-studio/ && \
    rm -rf /knowledge-graph-studio && \
    cd /repo && git checkout c41043506d095976b2d5b1c20dacf10cb8ad08bd && \
    pip install asgi_correlation_id==4.3.4 && \
    pip install fastapi==0.110.3 && \
    pip install spacy==3.8.3 && \
    pip install pydantic==2.10.3 && \
    pip install pydantic-settings==2.7.0 && \
    pip install uvicorn==0.34.0 && \
    pip install neo4j==5.27.0 && \
    pip install langchain==0.3.12 && \
    pip install langchain_community==0.3.12 && \
    pip install langchain_openai==0.2.12 && \
    pip install logfire[fastapi,pymongo,system-metrics]==2.7.1 && \
    pip install pypdf==5.1.0 && \
    pip install pinecone-client==5.0.1 && \
    pip install ipython==8.30.0 && \
    pip install python-multipart==0.0.20 && \
    pip install boto3==1.35.81 && \
    pip install datetime==5.5 && \
    pip install uuid==1.30 && \
    pip install pypdf2==3.0.1 && \
    pip install motor==3.4.0 && \
    pip install pymongo==4.8.0 && \
    pip install typer==0.15.1 && \
    pip install types-requests==2.32.0.20241016 && \
    pip install pyjwt[crypto]==2.10.1 && \
    pip install pytest-mock==3.14.0 && \
    pip install tiktoken==0.7.0 && \
    pip install auth0-python==4.7.1 && \
    pip install pandas==2.2.3
ENV PYTHONPATH=/repo/src
RUN cd /repo && pytest --collect-only -q