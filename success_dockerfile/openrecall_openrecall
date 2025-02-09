FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/openrecall/openrecall.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /openrecall/. /repo && rm -rf /openrecall/ && \
    rm -rf /openrecall && \
    cd /repo && git checkout 225a2750e3122718a9bad9c4d4ba4b0e99985c00 && \
    cd /repo && pip install -e . && \
    python /code_edit.py -t "/search_patch/0.patch"