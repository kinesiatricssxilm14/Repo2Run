FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/volfpeter/fasthx.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fasthx/. /repo && rm -rf /fasthx/ && \
    rm -rf /fasthx && \
    cd /repo && git checkout e850b9c61fa2c8868a0f7a4b2b567934c773eee8 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q