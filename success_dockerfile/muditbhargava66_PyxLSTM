FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/muditbhargava66/PyxLSTM.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /PyxLSTM/. /repo && rm -rf /PyxLSTM/ && \
    rm -rf /PyxLSTM && \
    cd /repo && git checkout f3c9bb80ac62f1b19bf196ab9b8045f33e8f849a && \
    pip install torch==2.5.1 && \
    pip install numpy==2.2.0 && \
    pip install pyyaml==6.0.2 && \
    pip install setuptools==65.5.1 && \
    pip install wheel==0.45.1 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-xdist==3.6.1 && \
    pip install pytest-timeout==2.3.1 && \
    pip install pytest-html==4.1.1 && \
    pip install ruff==0.8.3
RUN cd /repo && pytest --collect-only -q