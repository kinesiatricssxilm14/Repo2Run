FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jlowin/fastmcp.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fastmcp/. /repo && rm -rf /fastmcp/ && \
    rm -rf /fastmcp && \
    cd /repo && git checkout baa30086dad60a7dd530faee809d36d6ff7f5fa4 && \
    pip install hatchling==1.27.0 hatch-vcs==0.4.0 && \
    pip install hatch==1.14.0 && \
    cd /repo && hatch env create && \
    pip install pipreqs==0.5.0 && \
    pipreqs /repo --force --ignore examples && \
    pip install annotated_types==0.7.0 && \
    pip install httpx==0.28.1 && \
    pip install mcp==1.1.2 && \
    pip install pydantic==2.10.4 && \
    pip install pydantic_core==2.27.2 && \
    pip install pydantic_settings==2.7.0 && \
    pip install pytest==8.3.4 && \
    pip install python-dotenv==1.0.1 && \
    pip install rich==13.9.4 && \
    pip install starlette==0.42.0 && \
    pip install typer==0.15.1 && \
    pip install typing_extensions==4.12.2 && \
    pip install uvicorn==0.34.0
ENV PYTHONPATH=/repo/src:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    pip install -e /repo/src