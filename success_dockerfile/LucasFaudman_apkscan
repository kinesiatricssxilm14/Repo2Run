FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/LucasFaudman/apkscan.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /apkscan/. /repo && rm -rf /apkscan/ && \
    rm -rf /apkscan && \
    cd /repo && git checkout 3b3e622196e07566e630e3ad6687dc7574edf51b
ENV PYTHONPATH=/repo/src
RUN pip install enjarify-adapter==1.0.2 && \
    pip install pyyaml==6.0.2
ENV PYTHONPATH=/repo/src