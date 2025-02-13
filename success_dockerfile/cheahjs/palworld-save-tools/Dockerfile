FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/cheahjs/palworld-save-tools.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /palworld-save-tools/. /repo && rm -rf /palworld-save-tools/ && \
    rm -rf /palworld-save-tools && \
    cd /repo && git checkout 7dc2c72a5d15948ca5f52e000981e18b3404e3b9 && \
    pip install parameterized==0.9.0 mypy==1.8.0