FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/JosephBARBIERDARNAL/pypalettes.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /pypalettes/. /repo && rm -rf /pypalettes/ && \
    rm -rf /pypalettes && \
    cd /repo && git checkout 826930e1162dade99f31582af0cb00cc0d0e4261 && \
    cd /repo && pip install -e . && \
    pip install pandas==2.2.3
RUN cd /repo && pytest --collect-only -q