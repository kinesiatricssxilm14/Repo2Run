FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/weareprestatech/hotpdf.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /hotpdf/. /repo && rm -rf /hotpdf/ && \
    rm -rf /hotpdf && \
    cd /repo && git checkout 55ab97231a46d072aa33d2dd7cb2927e2c0d4e42 && \
    pip install pdfminer.six==20240706 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-xdist==3.6.1 && \
    pip install pylint==3.3.2 && \
    pip install mypy==1.13.0 && \
    pip install typing-extensions==4.12.2 && \
    pip install pre-commit==4.0.1 && \
    pip install ruff==0.8.3