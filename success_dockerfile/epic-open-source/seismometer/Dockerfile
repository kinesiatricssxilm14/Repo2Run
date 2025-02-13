FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/epic-open-source/seismometer.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /seismometer/. /repo && rm -rf /seismometer/ && \
    rm -rf /seismometer && \
    cd /repo && git checkout b3e812fdc7ea475de9991bedc493897d0215659a && \
    cd /repo && pip install -e .[dev]