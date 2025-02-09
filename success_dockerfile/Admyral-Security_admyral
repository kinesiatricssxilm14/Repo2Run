FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Admyral-Security/admyral.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /admyral/. /repo && rm -rf /admyral/ && \
    rm -rf /admyral && \
    cd /repo && git checkout de332e2dd7d1deb536d859b7ad7bf74f64ab7e93 && \
    cd /repo && poetry install && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch" && \
    python /code_edit.py -t "/search_patch/8.patch" && \
    python /code_edit.py -t "/search_patch/9.patch" && \
    python /code_edit.py -t "/search_patch/10.patch" && \
    python /code_edit.py -t "/search_patch/11.patch" && \
    python /code_edit.py -t "/search_patch/12.patch" && \
    python /code_edit.py -t "/search_patch/13.patch"
RUN cd /repo && poetry run pytest --collect-only -q