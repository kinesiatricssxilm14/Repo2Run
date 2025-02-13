FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/google-research/timesfm.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /timesfm/. /repo && rm -rf /timesfm/ && \
    rm -rf /timesfm && \
    cd /repo && git checkout 02bc2f2212887b2e3915b934b7af3347701bcf29 && \
    cd /repo && poetry install -E pax && \
    cd /repo && poetry install -E pax --no-root && \
    cd /repo && poetry run pip list