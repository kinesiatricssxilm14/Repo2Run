FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/igorbenav/SQLModel-boilerplate.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /SQLModel-boilerplate/. /repo && rm -rf /SQLModel-boilerplate/ && \
    rm -rf /SQLModel-boilerplate && \
    cd /repo && git checkout 2ead0414113a4f5b2b28183cef427c4e5b864284 && \
    cd /repo && poetry install && \
    touch /repo/.env && \
    ln -s /repo/.env /repo/src/app/.env && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    cd /repo && poetry add aiosqlite
RUN cd /repo && poetry run pytest --collect-only -q