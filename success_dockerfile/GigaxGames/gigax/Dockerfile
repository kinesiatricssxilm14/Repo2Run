FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/GigaxGames/gigax.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /gigax/. /repo && rm -rf /gigax/ && \
    rm -rf /gigax && \
    cd /repo && git checkout c3c209de6290f9f3f2f9395625bb2e8094122531 && \
    pip install -e /repo && \
    pip install python-dotenv==1.0.1 && \
    pip install pytest-asyncio==0.25.0 && \
    python /code_edit.py -t "/search_patch/0.patch"