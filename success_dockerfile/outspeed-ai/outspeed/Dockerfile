FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/outspeed-ai/outspeed.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /outspeed/. /repo && rm -rf /outspeed/ && \
    rm -rf /outspeed && \
    cd /repo && git checkout 049b40f38cf3e9716e980a2959cd0fd530cc7c99 && \
    cd /repo && poetry install && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    cd /repo && poetry lock && \
    cd /repo && poetry install && \
    cd /repo && poetry install -E silero