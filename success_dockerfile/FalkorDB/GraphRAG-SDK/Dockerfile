FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/FalkorDB/GraphRAG-SDK.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /GraphRAG-SDK/. /repo && rm -rf /GraphRAG-SDK/ && \
    rm -rf /GraphRAG-SDK && \
    cd /repo && git checkout 250ebec4c7d052248d27ca8c31f369c59a40ff78 && \
    cd /repo && poetry install && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    cd /repo && poetry lock && \
    cd /repo && poetry install && \
    cd /repo && poetry install -E google-generativeai -E vertexai -E ollama -E openai