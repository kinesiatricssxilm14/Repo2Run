FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Codium-ai/cover-agent.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /cover-agent/. /repo && rm -rf /cover-agent/ && \
    rm -rf /cover-agent && \
    cd /repo && git checkout 5c4b8878943df9a85d5d71b43d294e299b564110 && \
    pip install fastapi==0.115.6 pyyaml==6.0.2 jinja2==3.1.5 sqlalchemy==2.0.36 wandb==0.19.2
ENV PYTHONPATH=$PYTHONPATH:/repo/cover_agent
RUN pip install httpx==0.27.2 litellm==1.57.4 dynaconf==3.2.6 grep_ast==0.4.1 && \
    python /code_edit.py -t "/search_patch/4.patch"
ENV PYTHONPATH="/repo:$PYTHONPATH"
RUN pip install tenacity==9.0.0
ENV PYTHONPATH=/repo/cover_agent:$PYTHONPATH
RUN cd /repo && pytest --collect-only -q