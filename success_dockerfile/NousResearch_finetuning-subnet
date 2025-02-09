FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/NousResearch/finetuning-subnet.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /finetuning-subnet/. /repo && rm -rf /finetuning-subnet/ && \
    rm -rf /finetuning-subnet && \
    cd /repo && git checkout e2f5eb6373a417fc7c03e38adbc6cf145670ab58 && \
    pip install bittensor==8.5.1 && \
    pip install huggingface_hub==0.27.0 && \
    pip install matplotlib==3.10.0 && \
    pip install numpy==2.0.2 && \
    pip install pandas==2.2.3 && \
    pip install pydantic==2.10.3 && \
    pip install python-dotenv==1.0.1 && \
    pip install rich==13.9.4 && \
    pip install safetensors==0.4.5 && \
    pip install torch==2.5.1 && \
    pip install transformers==4.40.0 && \
    pip install wandb==0.19.1 && \
    pip install sentencepiece==0.2.0 && \
    pip install jinja2==3.1.4 && \
    pip install pydantic==1.7.4 && \
    pip install bittensor==8.5.1 -U
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch"