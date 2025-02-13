FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/InternLM/InternEvo.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /InternEvo/. /repo && rm -rf /InternEvo/ && \
    rm -rf /InternEvo && \
    cd /repo && git checkout 5ad2eb02fb5be2196e505600fef459185070d1e3 && \
    cd /repo && pip install -e . && \
    pip install torch==2.5.1 && \
    pip install pillow==11.1.0 && \
    apt-get update -qq && \
    apt-get install -y -qq rustc && \
    apt-get update -qq && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    . "$HOME/.cargo/env" && \
    pip install transformers==4.25.1
ENV share_path="/repo/shared_data"
RUN python /code_edit.py -t "/search_patch/0.patch"
RUN cd /repo && pytest --collect-only -q