FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/illuin-tech/colpali.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /colpali/. /repo && rm -rf /colpali/ && \
    rm -rf /colpali && \
    cd /repo && git checkout e45c4cc180ccfebd178997b34a569c8293b8bb8c && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    pip install GPUtil==1.4.0 && \
    pip install numpy==1.26.4 && \
    pip install peft==0.11.1 && \
    pip install pillow==10.4.0 && \
    pip install requests==2.32.3 && \
    pip install torch==2.5.1 && \
    pip install transformers==4.46.3 && \
    pip install accelerate==1.0.1 && \
    pip install bitsandbytes==0.45.0 && \
    pip install configue==6.0.0 && \
    pip install datasets==3.2.0 && \
    pip install mteb==1.16.5 && \
    pip install typer==0.15.1 && \
    pip install einops==0.8.0 && \
    pip install matplotlib==3.10.0 && \
    pip install seaborn==0.13.2 && \
    pip install pytest==8.3.4 && \
    pip install ruff==0.8.3
ENV PYTHONPATH=/repo/colpali_engine
ENV PYTHONPATH=/repo