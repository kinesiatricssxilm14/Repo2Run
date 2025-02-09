FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/cosmic-cortex/mlfz.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mlfz/. /repo && rm -rf /mlfz/ && \
    rm -rf /mlfz && \
    cd /repo && git checkout 5bf8d2ada262f95ab165f023cd7f8ba5a97f880c && \
    pip install numpy==2.2.0 && \
    pip install matplotlib==3.10.0 && \
    pip install seaborn==0.13.2 && \
    cd /repo && pip install -e . && \
    pip install scipy==1.14.1 && \
    pip install graphviz==0.20.3