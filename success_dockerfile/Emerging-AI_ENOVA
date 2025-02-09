FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Emerging-AI/ENOVA.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ENOVA/. /repo && rm -rf /ENOVA/ && \
    rm -rf /ENOVA && \
    cd /repo && git checkout b3661d06064ba1a46417f24c9e8ee8dec7e2fa03 && \
    pip install enova==0.0.7 && \
    pip install enova_instrumentation_llmo==0.0.7 && \
    pip install pytest==8.3.3 && \
    pip install pytest-asyncio==0.24.0
RUN cd /repo && pytest --collect-only -q