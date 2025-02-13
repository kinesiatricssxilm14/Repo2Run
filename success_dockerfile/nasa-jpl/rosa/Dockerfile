FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/nasa-jpl/rosa.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /rosa/. /repo && rm -rf /rosa/ && \
    rm -rf /rosa && \
    cd /repo && git checkout 5471dc2d2b942bdfeab79e5e5fd56f7a98c4c966 && \
    pip install python-dotenv==1.0.1 && \
    pip install pydantic==2.10.3 && \
    pip install pyinputplus==0.2.12 && \
    pip install azure-identity==1.19.0 && \
    pip install cffi==1.17.1 && \
    pip install rich==13.9.4 && \
    pip install pillow==11.0.0 && \
    pip install numpy==1.26.4 && \
    pip install langchain==0.3.9 && \
    pip install langchain-community==0.3.9 && \
    pip install langchain-core==0.3.21 && \
    pip install langchain-openai==0.2.11 && \
    pip install langchain-ollama==0.2.1 && \
    pip install pyyaml==6.0.2
RUN cd /repo && pytest --collect-only -q