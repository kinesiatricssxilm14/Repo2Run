FROM python:3.12
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Integuru-AI/Integuru.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Integuru/. /repo && rm -rf /Integuru/ && \
    rm -rf /Integuru && \
    cd /repo && git checkout 928e8285b5d6204dd30dec8fc7a56aabb53ba2a1 && \
    cd /repo && poetry install
ENV PYTHONPATH=/repo
RUN cd /repo && poetry add langchain-openai && \
    pip install langchain_openai==0.2.14
ENV PYTHONPATH=/repo
RUN pip install networkx==3.4.2
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q