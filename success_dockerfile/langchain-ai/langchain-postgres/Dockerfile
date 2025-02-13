FROM python:3.9
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/langchain-ai/langchain-postgres.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /langchain-postgres/. /repo && rm -rf /langchain-postgres/ && \
    rm -rf /langchain-postgres && \
    cd /repo && git checkout 064e5b9506da5f18cb1ccfdcca8ee54f2a089524 && \
    cd /repo && poetry install && \
    pip install langchain_core==0.3.29 && \
    pip install langchain_tests==0.3.7 && \
    pip install numpy==1.23.5 && \
    pip install pgvector==0.3.6 && \
    pip install psycopg==3.2.3 && \
    pip install pytest==8.3.4 && \
    pip install simsimd==6.2.1 && \
    pip install SQLAlchemy==1.4.39 && \
    pip install typing_extensions==4.12.2 && \
    cd /repo && poetry install --with test && \
    cd /repo && poetry install --sync && \
    cd /repo && pip install pytest==8.3.4 pytest-asyncio==0.25.2 pytest-socket==0.7.0 pytest-cov==6.0.0 pytest-timeout==2.3.1 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    pip show SQLAlchemy && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch"
RUN cd /repo && pytest --collect-only -q