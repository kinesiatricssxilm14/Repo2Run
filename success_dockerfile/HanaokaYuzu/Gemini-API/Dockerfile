FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/HanaokaYuzu/Gemini-API.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Gemini-API/. /repo && rm -rf /Gemini-API/ && \
    rm -rf /Gemini-API && \
    cd /repo && git checkout e8a2d232131b15a094a859827cc9a6278b2e4494 && \
    pip install -e /repo
RUN cd /repo && pytest --collect-only -q