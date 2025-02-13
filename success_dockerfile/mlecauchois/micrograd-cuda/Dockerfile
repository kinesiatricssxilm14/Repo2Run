FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/mlecauchois/micrograd-cuda.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /micrograd-cuda/. /repo && rm -rf /micrograd-cuda/ && \
    rm -rf /micrograd-cuda && \
    cd /repo && git checkout ab1ca09e61c9c311fab96cbfaf52c15769e9c36f && \
    pip install pytest==8.3.4
ENV PYTHONPATH=/repo/micrograd_cuda:$PYTHONPATH
RUN apt-get update -qq && \
    apt-get update -qq && \
    echo '#!/bin/bash' > /repo/compile_cuda.sh && \
    echo 'gcc -shared -o /repo/micrograd_cuda/liboperations.so /repo/micrograd_cuda/operations.cu' >> /repo/compile_cuda.sh && \
    chmod +x /repo/compile_cuda.sh && \
    apt-get update -qq && \
    apt-get update -qq && \
    pip install numpy==2.2.0 && \
    apt-get update -qq && \
    apt-cache search cuda && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch"
ENV PYTHONPATH=/repo/micrograd_cuda:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/3.patch"
ENV PYTHONPATH=/repo/micrograd_cuda:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/4.patch"
ENV PYTHONPATH=/repo/micrograd_cuda:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/5.patch"
ENV PYTHONPATH=/repo/micrograd_cuda:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/6.patch"
ENV PYTHONPATH=/repo/micrograd_cuda:$PYTHONPATH