FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/igorbenav/fastcrud.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fastcrud/. /repo && rm -rf /fastcrud/ && \
    rm -rf /fastcrud && \
    cd /repo && git checkout dc831b113302909db17dc61982cf217fb34005f3 && \
    cd /repo && poetry install && \
    python /code_edit.py -t "/search_patch/0.patch"
RUN cd /repo && poetry run pytest --collect-only -q