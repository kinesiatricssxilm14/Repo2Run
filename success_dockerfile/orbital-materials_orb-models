FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/orbital-materials/orb-models.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /orb-models/. /repo && rm -rf /orb-models/ && \
    rm -rf /orb-models && \
    cd /repo && git checkout 25157368a47faf424e76dc05217a6f0671810297 && \
    pip install cached_path==1.6.5 && \
    pip install ase==3.23.0 && \
    pip install scipy==1.14.1 && \
    pip install torch==2.2.0 && \
    pip install dm-tree==0.1.8 && \
    pip install tqdm==4.67.1 && \
    pip install numpy==2.2.0 && \
    pip install pytest==8.3.4 && \
    git config --global url."http://".insteadOf "https://" && \
    pip install git+https://github.com/dwastberg/pynanoflann#egg=pynanoflann