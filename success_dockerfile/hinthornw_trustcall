FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/hinthornw/trustcall.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /trustcall/. /repo && rm -rf /trustcall/ && \
    rm -rf /trustcall && \
    cd /repo && git checkout eaaaad1f8dfc1eba22cede42b3a9bf8be99ec9d0 && \
    pip install langgraph==0.2.59 && \
    pip install pytest-watch==4.2.0 && \
    pip install pytest-xdist==3.6.1 && \
    pip install anyio==4.7.0 && \
    pip install pytest-asyncio-cooperative==0.37.0 && \
    pip install jsonpatch==1.33 && \
    pip install pytest==7.1.2 && \
    pip install langchain==0.3.12 && \
    pip install dydantic==0.0.7 && \
    pip install langchain_core==0.3.25 && \
    pip install langgraph==0.2.59 && \
    pip install langsmith==0.2.3 && \
    pip install pydantic==2.10.3 && \
    pip install typing_extensions==4.12.2
ENV PYTHONPATH=$PYTHONPATH:/repo