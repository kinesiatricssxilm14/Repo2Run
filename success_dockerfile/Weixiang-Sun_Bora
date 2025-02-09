FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Weixiang-Sun/Bora.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Bora/. /repo && rm -rf /Bora/ && \
    rm -rf /Bora && \
    cd /repo && git checkout c08bb69db6752031d6b6e24757bc9b054ecf1d1c && \
    pip install colossalai==0.4.7 && \
    pip install accelerate==1.2.1 && \
    pip install diffusers==0.29.0 && \
    pip install ftfy==6.3.1 && \
    pip install gdown==5.2.0 && \
    pip install mmengine==0.10.5 && \
    pip install pre-commit==4.0.1 && \
    pip install pyav==14.0.1 && \
    pip install tensorboard==2.18.0 && \
    pip install timm==1.0.12 && \
    pip install tqdm==4.67.1 && \
    pip install transformers==4.39.3 && \
    pip install wandb==0.19.2
ENV PYTHONPATH=$PYTHONPATH:/repo/opensora
RUN pip install xformers==0.0.29.post1 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    cd /repo && pip install -e . && \
    cd /repo && pip install torch==2.5.1
RUN cd /repo && pytest --collect-only -q