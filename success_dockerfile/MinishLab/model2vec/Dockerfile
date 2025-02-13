FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/MinishLab/model2vec.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /model2vec/. /repo && rm -rf /model2vec/ && \
    rm -rf /model2vec && \
    cd /repo && git checkout 4e3fba3a44702c523c68ad7bd0b49fb0367909c8 && \
    pip install jinja2==3.1.4 && \
    pip install numpy==2.2.0 && \
    pip install rich==13.9.4 && \
    pip install safetensors==0.4.5 && \
    pip install setuptools==65.5.1 && \
    pip install tokenizers==0.21.0 && \
    pip install tqdm==4.67.1 && \
    pip install black==24.10.0 && \
    pip install ipython==8.30.0 && \
    pip install mypy==1.13.0 && \
    pip install pre-commit==4.0.1 && \
    pip install pytest==8.3.4 && \
    pip install pytest-coverage==0.0 && \
    pip install ruff==0.8.3 && \
    pip install torch==2.5.1 && \
    pip install transformers==4.47.0 && \
    pip install scikit-learn==1.6.0 && \
    pip install onnx==1.17.0 && \
    pip install -e /repo