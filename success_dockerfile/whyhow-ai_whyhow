FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/whyhow-ai/whyhow.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /whyhow/. /repo && rm -rf /whyhow/ && \
    rm -rf /whyhow && \
    cd /repo && git checkout 63a3c6c18e660ac5c7268159956f62db3f15a0ae && \
    pip install httpx==0.28.1 && \
    pip install pydantic==2.10.5 && \
    pip install bandit==1.8.0 && \
    pip install black==24.10.0 && \
    pip install flake8==7.1.1 && \
    pip install flake8-docstrings==1.7.0 && \
    pip install fpdf==1.7.2 && \
    pip install isort==5.13.2 && \
    pip install mypy==1.14.1 && \
    pip install pydocstyle==6.3.0 && \
    pip install pytest-asyncio==0.25.2 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-httpx==0.35.0 && \
    pip install pytest==8.3.4 && \
    pip install mkdocs==1.6.1 && \
    pip install mkdocstrings==0.27.0 && \
    pip install mkdocs-material==9.5.49 && \
    pip install pymdown-extensions==10.14
ENV PYTHONPATH=/repo/src
RUN cd /repo && pytest --collect-only -q