FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/etianen/logot.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /logot/. /repo && rm -rf /logot/ && \
    rm -rf /logot && \
    cd /repo && git checkout 54e5ef74a31ae7447a97621af8deda5489e2c4fa && \
    cd /repo && poetry install
ENV PYTHONPATH=/repo
RUN pip install loguru==0.7.3 && \
    pip install hypothesis==6.122.3 && \
    pip install structlog==24.4.0 && \
    pip install trio==0.27.0
ENV PYTHONPATH=/repo