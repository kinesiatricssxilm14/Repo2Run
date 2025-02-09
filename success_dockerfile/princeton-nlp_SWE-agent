FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/princeton-nlp/SWE-agent.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /SWE-agent/. /repo && rm -rf /SWE-agent/ && \
    rm -rf /SWE-agent && \
    cd /repo && git checkout 8b35715665a3e996002886ca94c603e2850fad6b && \
    pip install -e /repo