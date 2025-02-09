FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/koaning/uvtrick.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /uvtrick/. /repo && rm -rf /uvtrick/ && \
    rm -rf /uvtrick && \
    cd /repo && git checkout 2d7f279fd9915d981d4dda28c4361d6241134055 && \
    pip install cloudpickle==3.1.0 && \
    pip install uv==0.5.10 && \
    pip install pytest==8.3.4