FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/chernyadev/bigym.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /bigym/. /repo && rm -rf /bigym/ && \
    rm -rf /bigym && \
    cd /repo && git checkout 72d305437d5a13800ea633479a1060619fc14e54 && \
    cd /repo && pip install -e . && \
    apt-get update -qq && \
    apt-get install -y -qq libglu1-mesa-dev freeglut3-dev mesa-common-dev