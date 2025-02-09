FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/xhluca/bm25s.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /bm25s/. /repo && rm -rf /bm25s/ && \
    rm -rf /bm25s && \
    cd /repo && git checkout c4fef24f0e05bd5b0152308095c3585d2f6c9aba && \
    pip install -e /repo && \
    pip install beir==2.0.0 && \
    pip install stemmer==0.0.4 && \
    pip install tqdm==4.64.1 && \
    pip install numba==0.60.0 && \
    pip install pystemmer==2.2.0.3
ENV PYTHONPATH=/repo
ENV PYTHONPATH=/repo:/repo/tests/comparison
ENV PYTHONPATH=/repo:/repo/tests
RUN pip install bm25_pt==0.0.7 && \
    pip install huggingface_hub==0.10.1 && \
    pip install jax==0.4.37 && \
    pip install nltk==3.7 && \
    pip install numpy==1.23.5 && \
    pip install orjson==3.10.12 && \
    pip install PyStemmer==2.2.0.3 && \
    pip install pytrec_eval==0.5 && \
    pip install rank_bm25==0.2.2 && \
    pip install scipy==1.10.0 && \
    pip install setuptools==65.6.3 && \
    pip install tqdm==4.64.1 && \
    pip install transformers==4.24.0
ENV PYTHONPATH=/repo:/repo/tests
RUN pip install tqdm==4.64.1 && \
    pip install huggingface_hub==0.10.1 && \
    pip install numpy==1.23.5 && \
    pip install transformers==4.24.0
ENV PYTHONPATH=/repo:/repo/tests:/repo/tests/comparison
ENV PYTHONPATH=/repo:/repo/tests:/repo/tests/comparison:/repo/tests/core
RUN touch /repo/tests/comparison/__init__.py && \
    touch /repo/tests/core/__init__.py && \
    touch /repo/tests/comparison_full/__init__.py
ENV PYTHONPATH=/repo:/repo/tests:/repo/tests/comparison:/repo/tests/core:/repo/tests/comparison_full