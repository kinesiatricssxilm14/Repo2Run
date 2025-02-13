FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/arvindrajan92/DTrOCR.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /DTrOCR/. /repo && rm -rf /DTrOCR/ && \
    rm -rf /DTrOCR && \
    cd /repo && git checkout a10aa009efae6336372bf3cb0c87cdc303cddf74 && \
    pip install Pillow==10.4.0 && \
    pip install torch==2.3.1 && \
    pip install transformers==4.42.4