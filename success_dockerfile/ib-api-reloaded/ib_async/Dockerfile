FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ib-api-reloaded/ib_async.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ib_async/. /repo && rm -rf /ib_async/ && \
    rm -rf /ib_async && \
    cd /repo && git checkout 38cf54a66a4daefbd3fd1d7476381f0d178a8198 && \
    cd /repo && poetry install
ENV PYTHONPATH=$PYTHONPATH:/repo
RUN pip install eventkit==1.0.3 && \
    pip install -e /repo && \
    pip install pandas==2.2.3