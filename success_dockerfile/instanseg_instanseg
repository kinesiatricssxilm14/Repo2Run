FROM python:3.9
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/instanseg/instanseg.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /instanseg/. /repo && rm -rf /instanseg/ && \
    rm -rf /instanseg && \
    cd /repo && git checkout 0df8b263109b47b106900aef4b2ceca0129ffbb4 && \
    pip install bioio==1.1.0 && \
    pip install bioio-ome-tiff==1.0.1 && \
    pip install colorcet==3.1.0 && \
    pip install einops==0.8.0 && \
    pip install fastremap==1.15.0 && \
    pip install geojson==3.1.0 && \
    pip install matplotlib==3.9.4 && \
    pip install numpy==1.26.4 && \
    pip install palettable==3.3.3 && \
    pip install rasterio==1.4.3 && \
    pip install scikit-image==0.22.0 && \
    pip install slideio==2.6.5 && \
    pip install tifffile==2024.8.30 && \
    pip install tiffslide==2.4.0 && \
    pip install torch==2.5.1 && \
    pip install tqdm==4.67.1 && \
    pip install pytest==8.2.2 && \
    pip install coverage==7.6.9 && \
    pip install genbadge==1.1.1
ENV PYTHONPATH=/repo/instanseg
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q