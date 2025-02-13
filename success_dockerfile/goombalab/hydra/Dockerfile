FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/goombalab/hydra.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /hydra/. /repo && rm -rf /hydra/ && \
    rm -rf /hydra && \
    cd /repo && git checkout b6b9b799541826755f6f9edcc645afc2438e9ea0 && \
    pip install einops==0.8.0 && \
    pip install torch==2.5.1 && \
    pip install mosaicml[nlp,wandb]==0.28.0 && \
    pip install mosaicml-streaming==0.4.1 && \
    pip install omegaconf==2.3.0 && \
    pip install transformers==4.45.2
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch"
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/3.patch"
ENV PYTHONPATH=/repo:$PYTHONPATH