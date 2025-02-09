FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/codeintegrity-ai/mutahunter.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mutahunter/. /repo && rm -rf /mutahunter/ && \
    rm -rf /mutahunter && \
    cd /repo && git checkout f889227782892724393f416ced724497ca72aae6 && \
    pip install tree-sitter==0.21.3 tree_sitter_languages==1.10.2 tqdm==4.67.1 grep_ast==0.4.1 pygments==2.18.0 networkx==3.4.2 jinja2==3.1.4 litellm==1.55.3 numpy==2.2.0 scipy==1.14.1 isort==5.13.2 black==24.10.0 pytest==8.3.4 && \
    pip install fastapi==0.115.6
ENV PYTHONPATH=$PYTHONPATH:/repo/src