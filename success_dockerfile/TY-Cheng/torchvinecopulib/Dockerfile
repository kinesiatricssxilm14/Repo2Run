FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/TY-Cheng/torchvinecopulib.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /torchvinecopulib/. /repo && rm -rf /torchvinecopulib/ && \
    rm -rf /torchvinecopulib && \
    cd /repo && git checkout c3a477620259d238e6f8668e321063994c0832b2 && \
    cd /repo && poetry install && \
    pip install matplotlib==3.10.0 && \
    pip install pandas==2.2.3 && \
    pip install torch==2.5.1 && \
    pip install pyvinecopulib==0.6.8 && \
    pip install scipy==1.14.1
RUN cd /repo && pytest --collect-only -q