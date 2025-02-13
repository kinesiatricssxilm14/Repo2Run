FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/epogrebnyak/justpath.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /justpath/. /repo && rm -rf /justpath/ && \
    rm -rf /justpath && \
    cd /repo && git checkout 0aca516bba87253e19e8dc09ca17685e749c6a4f && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q