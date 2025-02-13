FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jonbarron/camp_zipnerf.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /camp_zipnerf/. /repo && rm -rf /camp_zipnerf/ && \
    rm -rf /camp_zipnerf && \
    cd /repo && git checkout 8e6d57e3aee34235faf3ef99decca0994efe66c9 && \
    pip install chex==0.1.85 dm-pix==0.4.2 ffmpeg==1.4 flax==0.7.5 gin-config==0.5.0 immutabledict==4.1.0 jax==0.4.23 jaxcam==0.1.1 jaxlib==0.4.23 mediapy==1.2.0 ml_collections==1.0.0 numpy==1.26.4 opencv-python==4.9.0.80 pillow==10.2.0 rawpy==0.19.0 scipy==1.11.0 tensorboard==2.15.1 tensorflow==2.15.1 && \
    apt-get update -qq && \
    apt-get install libgl1-mesa-glx -y -qq && \
    pip install pycolmap==3.11.1 && \
    pip show pycolmap && \
    python -c "import pycolmap; print(dir(pycolmap))" && \
    python /code_edit.py -t "/search_patch/0.patch"
RUN cd /repo && pytest --collect-only -q