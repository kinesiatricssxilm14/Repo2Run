FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/zeroasiccorp/logik.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /logik/. /repo && rm -rf /logik/ && \
    rm -rf /logik && \
    cd /repo && git checkout ca4bb129056c0b70a31720aec190b4670f20f238 && \
    pip install setuptools==65.5.1 siliconcompiler==0.29.0 pytest==8.3.3 pytest-timeout==2.3.1 flake8==7.1.1 Sphinx==8.1.3 sphinx-rtd-theme==3.0.2 autodocsumm==0.2.14
ENV PYTHONPATH=/repo/logik
RUN pip install -e /repo
RUN cd /repo && pytest --collect-only -q