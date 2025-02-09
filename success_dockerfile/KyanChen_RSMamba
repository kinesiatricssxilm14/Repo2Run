FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/KyanChen/RSMamba.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /RSMamba/. /repo && rm -rf /RSMamba/ && \
    rm -rf /RSMamba && \
    cd /repo && git checkout 3fa3056316f1412851e484384e9f206e0a11bf2b && \
    pip install einops==0.8.0 && \
    pip install importlib-metadata==8.5.0 && \
    pip install mat4py==0.6.0 && \
    pip install matplotlib==3.10.0 && \
    pip install modelindex==0.0.2 && \
    pip install numpy==2.2.0 && \
    pip install rich==13.9.4 && \
    pip install coverage==7.6.9 && \
    pip install interrogate==1.7.0 && \
    pip install albumentations==1.4.22 && \
    pip install requests==2.32.3 && \
    pip install scikit-learn==1.6.0 && \
    pip install pycocotools==2.0.8 && \
    pip install transformers==4.47.0 && \
    pip install mmcv==2.2.0 && \
    pip install mmengine==0.10.5 && \
    apt-get update -qq && \
    apt-get install libgl1 -y -qq && \
    pip install torch==2.5.1 && \
    pip install mmpretrain==1.2.0 && \
    pip install torchvision==0.20.1 && \
    python /code_edit.py -t "/search_patch/0.patch"