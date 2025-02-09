FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lmstudio-ai/venvstacks.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /venvstacks/. /repo && rm -rf /venvstacks/ && \
    rm -rf /venvstacks && \
    cd /repo && git checkout 235ce3b5ff2c323a6139d3a8ef66ad735dfcd69b && \
    pip install pdm==2.22.1 && \
    cd /repo && pdm install
ENV PYTHONPATH=/repo/src
RUN pip install click==8.1.8 && \
    pip install typer==0.15.1
ENV PYTHONPATH=/repo/src/venvstacks
ENV PYTHONPATH=/repo/src:/repo/src/venvstacks
RUN cd /repo && pytest --collect-only -q