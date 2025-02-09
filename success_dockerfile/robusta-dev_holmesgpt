FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/robusta-dev/holmesgpt.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /holmesgpt/. /repo && rm -rf /holmesgpt/ && \
    rm -rf /holmesgpt && \
    cd /repo && git checkout c4743a016866e2a216897518059d326e4d97aaa7 && \
    cd /repo && poetry install