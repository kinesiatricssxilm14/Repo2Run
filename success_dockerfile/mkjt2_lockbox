FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/mkjt2/lockbox.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /lockbox/. /repo && rm -rf /lockbox/ && \
    rm -rf /lockbox && \
    cd /repo && git checkout 58430d96d20afaa52f67e72cddd80ef56b79e7f8 && \
    cd /repo && poetry install