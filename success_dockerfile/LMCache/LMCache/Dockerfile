FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/LMCache/LMCache.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /LMCache/. /repo && rm -rf /LMCache/ && \
    rm -rf /LMCache && \
    cd /repo && git checkout 7d344359cdcdcb955924c77afe4a0d2fbe050fc6 && \
    pip install torch==2.5.1 && \
    pip install numpy==1.26.4 && \
    pip install pyyaml==6.0.2 && \
    pip install redis==5.2.1 && \
    pip install nvtx==0.2.10 && \
    pip install safetensors==0.4.5 && \
    pip install transformers==4.47.1 && \
    pip install yapf==0.40.0 && \
    pip install toml==0.10.2 && \
    pip install tomli==2.0.1 && \
    pip install ruff==0.6.5 && \
    pip install codespell==2.3.0 && \
    pip install isort==5.13.2 && \
    pip install clang-format==18.1.5 && \
    pip install mypy==1.11.2 && \
    pip install types-PyYAML==6.0.12.20240917 && \
    pip install types-requests==2.32.0.20241016 && \
    pip install types-setuptools==75.6.0.20241126 && \
    pip install pytest==8.3.4 && \
    pip install pytest-benchmark==5.1.0 && \
    pip install pytest-benchmark[histogram]==5.1.0 && \
    pip install buildkite-test-collector==0.1.9 && \
    apt-get update -qq
ENV CUDA_HOME=/usr/local/cuda
RUN python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch"
RUN cd /repo && pytest --collect-only -q