FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/TuragaLab/flybody.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /flybody/. /repo && rm -rf /flybody/ && \
    rm -rf /flybody && \
    cd /repo && git checkout 2e108868e777aeb9faa89ed107716b23079014c7 && \
    pip install numpy==1.26.4 && \
    pip install dm_control==1.0.26 && \
    pip install h5py==3.12.1 && \
    pip install pytest==8.3.4 && \
    pip install mediapy==1.2.2