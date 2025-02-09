FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/dottxt-ai/prompts.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /prompts/. /repo && rm -rf /prompts/ && \
    rm -rf /prompts && \
    cd /repo && git checkout 3d2689ad7c388af3ab603aa374a51ca66d9eb915 && \
    pip install jinja2==3.1.4 setuptools==65.5.1 setuptools_scm[toml]==8.1.0 && \
    pip install pre-commit==4.0.1 pytest==8.3.4 pytest-benchmark==5.1.0 mkdocs==1.6.1 mkdocs-material==9.5.49 mkdocs-section-index==0.3.9 mkdocs-git-committers-plugin-2==2.4.1 mkdocs-git-revision-date-localized-plugin==1.3.0
ENV PYTHONPATH=/repo