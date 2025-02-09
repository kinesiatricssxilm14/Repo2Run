FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/mixedbread-ai/baguetter.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /baguetter/. /repo && rm -rf /baguetter/ && \
    rm -rf /baguetter && \
    cd /repo && git checkout a6e9156613bef9f42b08e2ca3069a818284b60ba && \
    pip install autofaiss==2.17.0 && \
    pip install faiss-cpu==1.9.0.post1 && \
    pip install krovetzstemmer==0.8 && \
    pip install pystemmer==2.2.0.3 && \
    pip install nltk==3.9.1 && \
    pip install numba==0.60.0 && \
    pip install numpy==1.26.4 && \
    pip install optuna==4.1.0 && \
    pip install ranx==0.3.20 && \
    pip install scikit-learn==1.6.0 && \
    pip install tqdm==4.67.1 && \
    pip install unidecode==1.3.8 && \
    pip install usearch==2.16.6 && \
    pip install python-dotenv==1.0.1 && \
    pip install beir==2.0.0 && \
    pip install openpyxl==3.1.5 && \
    pip install datasets==3.2.0 && \
    pip install huggingface-hub==0.24.6 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install ipykernel==6.29.5 && \
    pip install ruff==0.8.3 && \
    pip install pre-commit==4.0.1 && \
    pip install uv==0.5.9 && \
    pip install jupyter==1.1.1 && \
    pip install notebook==7.3.1