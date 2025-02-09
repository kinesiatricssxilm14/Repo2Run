FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/paradigmxyz/spice.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /spice/. /repo && rm -rf /spice/ && \
    rm -rf /spice && \
    cd /repo && git checkout e962a9c435d2f990fe5684d6a876a8b13287f5ee && \
    pip install flit==3.10.1
ENV FLIT_ROOT_INSTALL=1
RUN cd /repo && flit install --deps all