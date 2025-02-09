FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/tahnok/colmi_r02_client.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /colmi_r02_client/. /repo && rm -rf /colmi_r02_client/ && \
    rm -rf /colmi_r02_client && \
    cd /repo && git checkout 84d3a6d9bd50cbac531d217ba1ff1cc7debe838d && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q