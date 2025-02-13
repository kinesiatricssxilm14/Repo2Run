FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/fpgmaas/cookiecutter-uv.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /cookiecutter-uv/. /repo && rm -rf /cookiecutter-uv/ && \
    rm -rf /cookiecutter-uv && \
    cd /repo && git checkout 90de47109fdfc8406847e4033a351a0118a4f7cd && \
    pip install uv==0.5.9 -U && \
    pip install cookiecutter==2.6.0 && \
    pip install pytest==8.3.4 && \
    pip install pre-commit==4.0.1 && \
    pip install pytest-cookies==0.7.0 && \
    pip install tox-uv==1.16.1 && \
    pip install deptry==0.21.1 && \
    pip install mypy==1.13.0 && \
    pip install pytest-cov==6.0.0 && \
    pip install ruff==0.8.3 && \
    pip install mkdocs==1.6.1 && \
    pip install mkdocs-material==9.5.49 && \
    pip install mkdocstrings[python]==0.27.0
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q