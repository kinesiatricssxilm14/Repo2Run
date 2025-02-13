FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/yihong0618/klingCreator.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /klingCreator/. /repo && rm -rf /klingCreator/ && \
    rm -rf /klingCreator && \
    cd /repo && git checkout e567c6a16cbeaec0411ea90bda6a0d932d3ee2a8 && \
    pip install -e /repo