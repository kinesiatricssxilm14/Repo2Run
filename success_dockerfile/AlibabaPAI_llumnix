FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/AlibabaPAI/llumnix.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /llumnix/. /repo && rm -rf /llumnix/ && \
    rm -rf /llumnix && \
    cd /repo && git checkout b319b23a197cc25e5e9a740c574c46be17fe9743 && \
    pip install vllm==0.4.2 && \
    pip install ray==2.40.0 && \
    pip install pyarrow==18.1.0 && \
    pip install aiohttp==3.11.10 && \
    pip install scipy==1.14.1 && \
    pip install pandas==2.2.3 && \
    pip install matplotlib==3.10.0 && \
    pip install func_timeout==4.3.5 && \
    pip install pyyaml==6.0.2 && \
    pip install yacs==0.1.8 && \
    pip install numpy==1.23.5 && \
    pip install pyzmq==26.2.0 && \
    cd /repo && pip install -e .