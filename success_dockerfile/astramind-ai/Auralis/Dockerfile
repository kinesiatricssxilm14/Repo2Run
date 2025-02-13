FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/astramind-ai/Auralis.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Auralis/. /repo && rm -rf /Auralis/ && \
    rm -rf /Auralis && \
    cd /repo && git checkout c357a1e5cb0aa816f7e63b1697957b8821f10bd3 && \
    pip install -e /repo && \
    apt-get update -qq && \
    apt-get install -y -qq portaudio19-dev && \
    pip install langid==1.1.6 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    apt-get update -qq && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch"
RUN cd /repo && pytest --collect-only -q