FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/basf/mamba-tabular.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mamba-tabular/. /repo && rm -rf /mamba-tabular/ && \
    rm -rf /mamba-tabular && \
    cd /repo && git checkout af1ea08a608cfbe945d33a22be4e2c63cbab311c && \
    pip install numpy==1.26.4 && \
    pip install pandas==2.2.3 && \
    pip install lightning==2.4.0 && \
    pip install scikit_learn==1.6.0 && \
    pip install torch==2.5.1 && \
    pip install torchmetrics==1.6.0 && \
    pip install setuptools==65.5.1 && \
    pip install properscoring==0.1 && \
    pip install scikit-optimize==0.10.2 && \
    pip install -e /repo && \
    touch /repo/mambular/utils/preprocessor.py && \
    python /code_edit.py -t "/search_patch/0.patch"