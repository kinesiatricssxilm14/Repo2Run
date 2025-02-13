FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/mistralai/mistral-common.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mistral-common/. /repo && rm -rf /mistral-common/ && \
    rm -rf /mistral-common && \
    cd /repo && git checkout 5cac5e1c05d9e6782bec49310e43f294649bc1e2 && \
    cd /repo && poetry install