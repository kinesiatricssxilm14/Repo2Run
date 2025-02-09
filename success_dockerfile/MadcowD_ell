FROM python:3.12
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/MadcowD/ell.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ell/. /repo && rm -rf /ell/ && \
    rm -rf /ell && \
    cd /repo && git checkout 36ca5eea1a5d4c266071d6a50848ad154034c44d && \
    cd /repo/x/openai_realtime && poetry install && \
    pip install numpy==2.1.3 && \
    pip install pydantic==2.10.3 && \
    pip install sqlalchemy==2.0.36 && \
    pip install ell-ai[all]==0.0.15 && \
    cd /repo/x/openai_realtime && pip install -e .
RUN cd /repo && pytest --collect-only -q