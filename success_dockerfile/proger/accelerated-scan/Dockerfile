FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/proger/accelerated-scan.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /accelerated-scan/. /repo && rm -rf /accelerated-scan/ && \
    rm -rf /accelerated-scan && \
    cd /repo && git checkout db7145f89a442ff0cef076d07f2ccc93c403b1c2 && \
    pip install hatch==1.14.0 && \
    cd /repo && hatch run pip install torch>=2.1.0 && \
    pip install torch==2.5.1
ENV PYTHONPATH=/repo
RUN apt-get update -qq && \
    apt-get install -y -qq ninja-build
ENV PYTHONPATH=/repo
ENV CUDA_HOME=/usr/local/cuda
ENV PYTHONPATH=/repo
RUN python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=/repo
RUN python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q