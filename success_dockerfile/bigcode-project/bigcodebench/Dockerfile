FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/bigcode-project/bigcodebench.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /bigcodebench/. /repo && rm -rf /bigcodebench/ && \
    rm -rf /bigcodebench && \
    cd /repo && git checkout aa634d5d4a067c979582ba6f28e2bcb588fd4246 && \
    cd /repo && pip install -e . && \
    ln -s /repo/bigcodebench/sanitize.py /repo/bigcodebench/legacy_sanitize.py && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    ln -s /repo/bigcodebench/legacy_sanitize.py /repo/bigcodebench/lecacy_sanitize.py && \
    python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch" && \
    python /code_edit.py -t "/search_patch/8.patch" && \
    python /code_edit.py -t "/search_patch/9.patch" && \
    python /code_edit.py -t "/search_patch/10.patch" && \
    python /code_edit.py -t "/search_patch/11.patch" && \
    python /code_edit.py -t "/search_patch/12.patch" && \
    python /code_edit.py -t "/search_patch/13.patch" && \
    python /code_edit.py -t "/search_patch/14.patch" && \
    python /code_edit.py -t "/search_patch/15.patch"