FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/arcee-ai/fastmlx.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fastmlx/. /repo && rm -rf /fastmlx/ && \
    rm -rf /fastmlx && \
    cd /repo && git checkout fd37bc8f8400ce98baf601dcc9b66e14f2618382 && \
    pip install mlx==0.18.0 && \
    pip install mlx-lm==0.19.2 && \
    pip install mlx-vlm==0.0.15 && \
    pip install fastapi==0.115.6 && \
    pip install jinja2==3.1.4