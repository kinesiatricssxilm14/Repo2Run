FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/dleemiller/WordLlama.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /WordLlama/. /repo && rm -rf /WordLlama/ && \
    rm -rf /WordLlama && \
    cd /repo && git checkout e38d4760a7e974d02d2556148d95b9053555d82d && \
    pip install -e /repo