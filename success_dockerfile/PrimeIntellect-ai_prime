FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/PrimeIntellect-ai/prime.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /prime/. /repo && rm -rf /prime/ && \
    rm -rf /prime && \
    cd /repo && git checkout a974cf5b66733dc7dc685e92f91377e51dcb2bf7 && \
    cd /repo && pip install hatchling==1.27.0 && \
    pip install poetry==2.0.0 && \
    pip install torch==2.5.1 && \
    pip install numpy==2.2.1 && \
    pip install setuptools==65.5.1 && \
    pip install transformers==4.47.1 && \
    pip install datasets==3.2.0 && \
    pip install einops==0.8.0 && \
    pip install torchdata==0.10.1 && \
    pip install fsspec[gcs]==2024.9.0 && \
    pip install ninja==1.11.1.3 && \
    pip install zstandard==0.23.0 && \
    pip install pyarrow==18.1.0 && \
    pip install toposolve==0.1.17 && \
    pip install psutil==6.1.1 && \
    pip install "git+https://github.com/samsja/pydantic_config.git@74c94ee"
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install gloo==0.1.2 && \
    pip install faker==33.3.0 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    pip install -e /repo/src && \
    apt-get update -qq && \
    apt-get install -y -qq libgloo-dev
RUN cd /repo && poetry run pytest --collect-only -q
RUN cd /repo && pytest --collect-only -q