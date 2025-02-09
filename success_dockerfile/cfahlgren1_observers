FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/cfahlgren1/observers.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /observers/. /repo && rm -rf /observers/ && \
    rm -rf /observers && \
    cd /repo && git checkout d46fdbfbb185f612de1a86f18c2941c6d79d38a6 && \
    pip install pdm==2.22.1 && \
    cd /repo && pdm install && \
    pip install openai==1.59.5 && \
    pip install observers==0.1.4
ENV PYTHONPATH="${PYTHONPATH}:/repo/src"
RUN cd /repo && pytest --collect-only -q