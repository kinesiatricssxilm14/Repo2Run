FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/igrek51/wat.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /wat/. /repo && rm -rf /wat/ && \
    rm -rf /wat && \
    cd /repo && git checkout 0d60790bc232b20514f8096f157423c6117c51a2 && \
    pip install setuptools==72.1.0 && \
    pip install setuptools_scm==8.1.0 && \
    pip install build==1.2.1 && \
    pip install pytest==8.2.0 && \
    pip install coverage==7.5.1 && \
    pip install twine==5.1.1 && \
    pip install wheel==0.43.0 && \
    pip install mkdocs==1.6.0 && \
    pip install mkdocs-material==9.5.22 && \
    pip install backoff==2.2.1 && \
    pip install pydantic==2.7.1 && \
    pip install nuclear==2.3.1
ENV PYTHONPATH=/repo