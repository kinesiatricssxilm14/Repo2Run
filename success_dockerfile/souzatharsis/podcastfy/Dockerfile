FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/souzatharsis/podcastfy.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /podcastfy/. /repo && rm -rf /podcastfy/ && \
    rm -rf /podcastfy && \
    cd /repo && git checkout 804a6188a74ab9cf088032f6e460a04ea968a97a && \
    cd /repo && poetry install