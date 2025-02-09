FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/genomoncology/FuzzTypes.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /FuzzTypes/. /repo && rm -rf /FuzzTypes/ && \
    rm -rf /FuzzTypes && \
    cd /repo && git checkout d962438ef706d189a0bf18b4b4129a72dee436c5 && \
    pip install annotated-types==0.6.0 && \
    pip install pydantic==2.6.2 && \
    pip install pydantic-core==2.16.3 && \
    pip install typing-extensions==4.9.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-mock==3.14.0 && \
    pip install coverage[toml]==7.6.10 && \
    pip install build==1.2.2.post1 && \
    pip install jupyter==1.1.1 && \
    pip install ipython==8.31.0 && \
    pip install mypy==1.14.1 && \
    pip install pip==24.3.1 && \
    pip install setuptools==65.5.1 && \
    pip install twine==6.0.1 && \
    pip install anyascii==0.3.2 && \
    pip install dateparser==1.2.0 && \
    pip install emoji==2.14.0 && \
    pip install lancedb==0.17.0 && \
    pip install nameparser==1.1.3 && \
    pip install number-parser==0.3.2 && \
    pip install rapidfuzz==3.11.0 && \
    pip install sentence-transformers==3.3.1 && \
    pip install tantivy==0.22.0 && \
    pip install unidecode==1.3.8
ENV PYTHONPATH=/repo/src
RUN cd /repo && pytest --collect-only -q