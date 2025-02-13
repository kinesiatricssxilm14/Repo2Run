FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/codematrixer/hmdriver2.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /hmdriver2/. /repo && rm -rf /hmdriver2/ && \
    rm -rf /hmdriver2 && \
    cd /repo && git checkout c0d07532fd1dd878f83f95a4d543a9281cc344ad && \
    cd /repo && poetry install
RUN cd /repo && pytest --collect-only -q