FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/cremebrule/digital-cousins.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /digital-cousins/. /repo && rm -rf /digital-cousins/ && \
    rm -rf /digital-cousins && \
    cd /repo && git checkout 49400bb4aca50eea97490c9c9f1b4431e50792dd && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install xformers==0.0.28.post3 && \
    pip install shapely==2.0.6 && \
    pip install open3d==0.18.0 && \
    pip install Pillow==11.0.0 && \
    pip install fpsample==0.3.3 && \
    pip install scikit-image==0.25.0 && \
    cd /repo && pip install -e . && \
    apt-get update -qq && \
    apt-get install -y -qq cmake && \
    pip install robomimic==0.3.0 && \
    pip install omnigibson==1.1.1 && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1
ENV CUDA_VISIBLE_DEVICES=
RUN python /code_edit.py -t "/search_patch/0.patch" && \
    pip install supervision==0.25.1