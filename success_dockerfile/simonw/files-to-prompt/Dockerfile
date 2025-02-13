FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/simonw/files-to-prompt.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /files-to-prompt/. /repo && rm -rf /files-to-prompt/ && \
    rm -rf /files-to-prompt && \
    cd /repo && git checkout f9a4d8fa20aa978c3502c94de335b44e57ac0a61 && \
    pip install click==8.1.7 && \
    pip install pytest==8.3.4 && \
    pip install -e /repo