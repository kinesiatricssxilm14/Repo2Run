FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/tox-dev/tox-uv.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /tox-uv/. /repo && rm -rf /tox-uv/ && \
    rm -rf /tox-uv && \
    cd /repo && git checkout d7405a6ed4f35d0ae525009cc1cd298fe2bc4bf4 && \
    pip install pytest==7.1.2 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-mock==3.14.0 && \
    pip install packaging==24.2 && \
    pip install pytest==7.1.2 && \
    pip install tox==4.23.2 && \
    pip install typing_extensions==4.12.2 && \
    pip install uv==0.5.9 && \
    pip install virtualenv==20.28.0 && \
    pip list && \
    pip install tox-uv==1.16.1
ENV PATH=$PATH:/root/.local/bin
RUN pip install devpi-process==1.0.2