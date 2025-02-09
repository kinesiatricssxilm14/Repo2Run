FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/microsoft/aurora.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /aurora/. /repo && rm -rf /aurora/ && \
    rm -rf /aurora && \
    cd /repo && git checkout 8b11659b91d06f87c2d22e541dbcd0092baf2157 && \
    pip install huggingface-hub==0.26.5 && \
    pip install numpy==2.2.0 && \
    pip install scipy==1.14.1 && \
    pip install torch==2.5.1 && \
    pip install einops==0.8.0 && \
    pip install timm==0.6.13 && \
    pip install wheel==0.45.1 && \
    pip install build==1.2.2.post1 && \
    pip install ghp-import==2.1.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install mypy==1.13.0 && \
    pip install ruff==0.4.1 && \
    pip install pre-commit==4.0.1 && \
    pip install jupyter-book==1.0.3
RUN cd /repo && pytest --collect-only -q