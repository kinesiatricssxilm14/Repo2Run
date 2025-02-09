FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/whyhow-ai/rule-based-retrieval.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /rule-based-retrieval/. /repo && rm -rf /rule-based-retrieval/ && \
    rm -rf /rule-based-retrieval && \
    cd /repo && git checkout 91701f45822823d6c54cac3b526e43cdb409e4e3 && \
    pip install langchain_core==0.3.27 langchain_community==0.3.13 langchain_openai==0.2.13 langchain_text_splitters==0.3.4 openai==1.58.1 pinecone-client==5.0.1 pydantic==2.10.4 pypdf==5.1.0 tiktoken==0.8.0 qdrant-client==1.12.1 && \
    pip install bandit[toml]==1.8.0 black==24.10.0 flake8==7.1.1 flake8-docstrings==1.7.0 fpdf==1.7.2 isort==5.13.2 mypy==1.13.0 pydocstyle[toml]==6.3.0 pytest-cov==6.0.0 pytest==8.3.4
ENV PYTHONPATH=/repo/src
RUN cd /repo && pytest --collect-only -q