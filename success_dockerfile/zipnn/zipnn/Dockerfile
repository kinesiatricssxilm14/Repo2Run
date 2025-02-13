FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/zipnn/zipnn.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /zipnn/. /repo && rm -rf /zipnn/ && \
    rm -rf /zipnn && \
    cd /repo && git checkout 187f336b6790cc66d1248befa52066937d185afd && \
    cd /repo && pip install -e . && \
    cd /repo && python3 -m unittest discover -s tests/ -p test_suit.py
RUN cd /repo && pytest --collect-only -q