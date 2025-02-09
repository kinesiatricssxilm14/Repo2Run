FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/darrenburns/posting.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /posting/. /repo && rm -rf /posting/ && \
    rm -rf /posting && \
    cd /repo && git checkout 94feabc232da078c8cc9194e5259c3cd2206cfbb && \
    pip install hatchling==1.27.0 hatch==1.14.0 && \
    cd /repo && hatch env create
ENV PYTHONPATH=/repo/src:$PYTHONPATH
RUN pip install textual==0.86.2 && \
    pip install pydantic==2.10.4
ENV PYTHONPATH=/repo/src
RUN pip install pyyaml==6.0.2
ENV PYTHONPATH=/repo/src
RUN pip install python-dotenv==1.0.1
ENV PYTHONPATH=/repo/src
RUN cd /repo && hatch env create
ENV PYTHONPATH=/repo/src
RUN python -m venv /repo/venv && \
    pip install textual[syntax]==0.86.2 && \
    pip install textual-autocomplete==3.0.0a13 && \
    pip install watchfiles==1.0.3 && \
    pip install pytest==8.3.4 && \
    pip install jinja2==3.1.5 && \
    pip install syrupy==4.8.0 && \
    pip install pytest-xdist==3.6.1 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-textual-snapshot==1.0.0 && \
    pip install mkdocs-material==9.5.49 && \
    pip install xdg-base-dirs==6.0.2
ENV PYTHONPATH=/repo/src
RUN python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    pip install -e /repo/src
ENV PYTHONPATH=/repo/src
RUN pip install click-default-group==1.2.4
ENV PYTHONPATH=/repo/src
RUN pip install pydantic-settings==2.7.1
ENV PYTHONPATH=/repo/src
RUN cd /repo && pytest --collect-only -q