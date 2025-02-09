FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/neuralmagic/guidellm.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /guidellm/. /repo && rm -rf /guidellm/ && \
    rm -rf /guidellm && \
    cd /repo && git checkout ecf2984645202eea022cc7c9f245947e2dd5457d && \
    pip install -e /repo && \
    pip install requests-mock==1.12.1 && \
    pip install scipy==1.14.1