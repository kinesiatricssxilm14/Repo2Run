FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/filipstrand/mflux.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mflux/. /repo && rm -rf /mflux/ && \
    rm -rf /mflux && \
    cd /repo && git checkout 627398f531b10f447406377355aad8f1665c6805 && \
    pip install huggingface-hub==0.27.0 && \
    pip install mlx==0.18.0 && \
    pip install numpy==2.2.0 && \
    pip install opencv-python==4.10.0.84 && \
    pip install piexif==1.1.3 && \
    pip install pillow==10.4.0 && \
    pip install safetensors==0.4.5 && \
    pip install sentencepiece==0.2.0 && \
    pip install tqdm==4.67.1 && \
    pip install transformers==4.47.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-timer==1.0.0
ENV PYTHONPATH="/repo/src:$PYTHONPATH"
RUN apt-get update -qq && \
    apt-get install libgl1-mesa-glx -y -qq && \
    pip install mlx==0.18.0 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    pip install -e /repo