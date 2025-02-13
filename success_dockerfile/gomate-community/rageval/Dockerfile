FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/gomate-community/rageval.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /rageval/. /repo && rm -rf /rageval/ && \
    rm -rf /rageval && \
    cd /repo && git checkout 01e2580efe714b3130602e02a7e7b017d16d79a2 && \
    cd /repo && pip install -e . && \
    pip install sacrebleu==2.4.3 && \
    pip install bert_score==0.3.13
RUN cd /repo && pytest --collect-only -q