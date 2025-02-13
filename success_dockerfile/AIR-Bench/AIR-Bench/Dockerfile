FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/AIR-Bench/AIR-Bench.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /AIR-Bench/. /repo && rm -rf /AIR-Bench/ && \
    rm -rf /AIR-Bench && \
    cd /repo && git checkout 4b27b8a8f2047a963805fcf6fb9d74be51ec440c && \
    pip install datasets==3.2.0 rich==13.9.4 pytrec_eval==0.5 && \
    pip install black==24.10.0 isort==5.13.2 pytest==8.3.4
ENV PYTHONPATH=/repo