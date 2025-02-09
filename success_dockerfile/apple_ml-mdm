FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/apple/ml-mdm.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ml-mdm/. /repo && rm -rf /ml-mdm/ && \
    rm -rf /ml-mdm && \
    cd /repo && git checkout 9a5632cffc74a7c72075611fb99aca9816291db1 && \
    cd /repo && pip install -e . && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install tensorboard==2.18.0 && \
    mkdir -p /repo/tests/data && \
    touch /repo/tests/data/bert.vocab && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    touch /repo/tests/data/t5.vocab && \
    pip install tensorboardx==2.6.2.2 && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    touch /repo/tests/data/imagenet.vocab