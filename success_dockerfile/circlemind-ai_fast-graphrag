FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/circlemind-ai/fast-graphrag.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fast-graphrag/. /repo && rm -rf /fast-graphrag/ && \
    rm -rf /fast-graphrag && \
    cd /repo && git checkout 447511679aeb68d06558b63ba8c434e56caaefce && \
    cd /repo && poetry install && \
    pip install pipreqs==0.5.0 && \
    pipreqs /repo/fast_graphrag --force && \
    pip install hnswlib==0.8.0 && \
    pip install instructor==1.7.0 && \
    pip install numpy==2.2.0 && \
    pip install openai==1.57.4 && \
    pip install pydantic==2.10.3 && \
    pip install python_igraph==0.11.8 && \
    pip install scipy==1.14.1 && \
    pip install tenacity==9.0.0 && \
    pip install tqdm==4.67.1 && \
    pip install xxhash==3.5.0