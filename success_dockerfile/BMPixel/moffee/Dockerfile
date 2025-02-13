FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/BMPixel/moffee.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /moffee/. /repo && rm -rf /moffee/ && \
    rm -rf /moffee && \
    cd /repo && git checkout 0e643d92cc1324fc7c8a924ee808e374fc662a1b && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q