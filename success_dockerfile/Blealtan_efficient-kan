FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Blealtan/efficient-kan.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /efficient-kan/. /repo && rm -rf /efficient-kan/ && \
    rm -rf /efficient-kan && \
    cd /repo && git checkout 7b6ce1c87f18c8bc90c208f6b494042344216b11 && \
    pip install pdm==2.22.0 && \
    cd /repo && pdm install && \
    pip install torch==2.5.1 && \
    pip install tqdm==4.67.1
ENV PYTHONPATH=$PYTHONPATH:/repo/src