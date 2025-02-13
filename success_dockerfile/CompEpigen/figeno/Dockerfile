FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/CompEpigen/figeno.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /figeno/. /repo && rm -rf /figeno/ && \
    rm -rf /figeno && \
    cd /repo && git checkout 14b904ae291728ca12780fcf8205212b9681dad0 && \
    pip install cooler==0.10.2 && \
    pip install filedialpy==1.3.0 && \
    pip install Flask==3.1.0 && \
    pip install h5py==3.7.0 && \
    pip install importlib_resources==6.4.5 && \
    pip install matplotlib==3.7.0 && \
    pip install numpy==1.23.5 && \
    pip install pandas==1.5.3 && \
    pip install pyBigWig==0.3.23 && \
    pip install pysam==0.22.1 && \
    pip install sphinx_rtd_theme==3.0.2 && \
    pip install vcfpy==0.13.8 && \
    pip install -e /repo