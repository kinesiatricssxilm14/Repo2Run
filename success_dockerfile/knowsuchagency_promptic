FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/knowsuchagency/promptic.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /promptic/. /repo && rm -rf /promptic/ && \
    rm -rf /promptic && \
    cd /repo && git checkout a1930cdb8e8d1a595a7f554ec16867f8ea1324da && \
    pip install flit==3.10.1
ENV FLIT_ROOT_INSTALL=1
RUN cd /repo && flit install --deps=all && \
    pip install tenacity==9.0.0