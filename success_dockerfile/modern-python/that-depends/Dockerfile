FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/modern-python/that-depends.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /that-depends/. /repo && rm -rf /that-depends/ && \
    rm -rf /that-depends && \
    cd /repo && git checkout 65e6569d69e97e7c3edecde0d817df0b77b1af8e && \
    pip install fastapi==0.115.6 litestar==2.13.0 httpx==0.28.0 pytest==8.3.3 pytest-cov==6.0.0 pytest-asyncio==0.24.0 pytest-repeat==0.9.3 ruff==0.8.1 mypy==1.13.0 typing-extensions==4.12.2 pre-commit==4.0.1