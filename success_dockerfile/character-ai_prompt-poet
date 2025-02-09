FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/character-ai/prompt-poet.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /prompt-poet/. /repo && rm -rf /prompt-poet/ && \
    rm -rf /prompt-poet && \
    cd /repo && git checkout 4664320754eb7789f69820ce6bd8108279524a44 && \
    cd /repo && pip install -e .