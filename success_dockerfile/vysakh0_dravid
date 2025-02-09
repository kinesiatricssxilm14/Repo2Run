FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/vysakh0/dravid.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /dravid/. /repo && rm -rf /dravid/ && \
    rm -rf /dravid && \
    cd /repo && git checkout 25b03bfcf5327be83be0a9721fb24ac7d7157eed && \
    cd /repo && poetry install && \
    echo "from .server_monitor import DevServerMonitor" >> /repo/src/drd/cli/monitor/__init__.py && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    cd /repo/src/drd/cli/monitor && git restore server_monitor.py && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    echo "from .main import run_dev_server_with_monitoring  __all__ = ['run_dev_server_with_monitoring'] from .server_monitor import DevServerMonitor" > /repo/src/drd/cli/monitor/__init__.py && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch"
RUN cd /repo && poetry run pytest --collect-only -q