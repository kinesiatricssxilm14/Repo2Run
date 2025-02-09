FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/SpecterOps/cred1py.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /cred1py/. /repo && rm -rf /cred1py/ && \
    rm -rf /cred1py && \
    cd /repo && git checkout 432f9107b8ac501a743b487de182e3ba0bd3023f && \
    pip install pycryptodome==3.21.0 && \
    pip install scapy==2.6.0