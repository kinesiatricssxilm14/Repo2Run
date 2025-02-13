FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/instructlab/instructlab.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /instructlab/. /repo && rm -rf /instructlab/ && \
    rm -rf /instructlab && \
    cd /repo && git checkout c978b2928c767cd14b221a965bdb5864c128d05c && \
    cd /repo && pip install -e .