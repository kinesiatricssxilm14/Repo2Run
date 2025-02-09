FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jxnl/n-levels-of-rag.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /n-levels-of-rag/. /repo && rm -rf /n-levels-of-rag/ && \
    rm -rf /n-levels-of-rag && \
    cd /repo && git checkout 2ce1106b0163d11fcf7959187b42f0d3a67fbe05 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    cd /repo && poetry install && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    cd /repo && poetry lock && \
    cd /repo && poetry install