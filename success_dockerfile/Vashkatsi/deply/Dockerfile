FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Vashkatsi/deply.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /deply/. /repo && rm -rf /deply/ && \
    rm -rf /deply && \
    cd /repo && git checkout 6d6875f01267fa99cfacf96706e160248ba2b82a
ENV PYTHONPATH=/repo
ENV PYTHONPATH=$(pwd)
RUN pip install PyYAML==6.0.2 && \
    pip install setuptools==65.6.3