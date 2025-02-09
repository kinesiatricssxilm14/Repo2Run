FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/mikekelly/AgentK.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /AgentK/. /repo && rm -rf /AgentK/ && \
    rm -rf /AgentK && \
    cd /repo && git checkout e9ec892bddeb0b9afd77fbb130f0a89c5b715cb7 && \
    pip install langgraph==0.2.0 && \
    pip install langchain-community==0.2.11 && \
    pip install langgraph-checkpoint==2.0.9 && \
    pip install langchain-openai==0.2.14 && \
    pip install langchain-anthropic==0.3.1 && \
    pip install langgraph-checkpoint-sqlite==2.0.1 && \
    pip install selenium==4.27.1 && \
    pip install unstructured==0.16.12 && \
    pip install duckduckgo-search==7.2.1 && \
    pip install python-dotenv==1.0.1
ENV PYTHONPATH=/repo
ENV OPENAI_API_KEY=dummy_key
ENV PYTHONPATH=/repo
ENV OPENAI_API_KEY=dummy_key
RUN cd /repo && pytest --collect-only -q