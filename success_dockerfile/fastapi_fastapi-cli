FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/fastapi/fastapi-cli.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fastapi-cli/. /repo && rm -rf /fastapi-cli/ && \
    rm -rf /fastapi-cli && \
    cd /repo && git checkout bc08401cf9c030dff0070dd9b944bf9f13bfd225 && \
    pip install pre-commit==4.0.1 && \
    pip install typer==0.15.1 && \
    pip install uvicorn[standard]==0.34.0 && \
    pip install rich-toolkit==0.12.0
ENV PYTHONPATH=/repo/src:$PYTHONPATH
RUN cd /repo && pytest --collect-only -q