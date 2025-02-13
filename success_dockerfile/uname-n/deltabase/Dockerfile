FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/uname-n/deltabase.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /deltabase/. /repo && rm -rf /deltabase/ && \
    rm -rf /deltabase && \
    cd /repo && git checkout 5eafb9d05316d005e2888cd1a1c71bf01e5f4e0f && \
    cd /repo && poetry install && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    cd /repo && poetry lock && \
    cd /repo && poetry install