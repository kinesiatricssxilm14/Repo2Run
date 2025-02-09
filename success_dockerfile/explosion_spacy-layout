FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/explosion/spacy-layout.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /spacy-layout/. /repo && rm -rf /spacy-layout/ && \
    rm -rf /spacy-layout && \
    cd /repo && git checkout 470c6dba7f1f8a1e52eb43f9925764cad1b1de1a && \
    pip install spacy==3.8.2 && \
    pip install docling==2.8.3 && \
    pip install pytest==8.3.3 && \
    cd /repo && pip install -e .