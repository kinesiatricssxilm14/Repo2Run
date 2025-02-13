FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/IST-DASLab/PanzaMail.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /PanzaMail/. /repo && rm -rf /PanzaMail/ && \
    rm -rf /PanzaMail && \
    cd /repo && git checkout b1807c814a4877daba040e09239849e7513135fb && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    pip install torch==2.2.2 && \
    pip install ollama==0.4.4 && \
    pip install omegaconf==2.3.0 && \
    pip install fastapi==0.115.6 && \
    pip install uvicorn==0.34.0 && \
    pip install pydantic==2.10.3 && \
    pip install python-dotenv==1.0.1 && \
    pip install hydra-core==1.3.2 && \
    pip install langchain==0.3.12 && \
    pip install langchain-community==0.3.12 && \
    pip install sentence-transformers==3.3.1 && \
    pip install faiss-cpu==1.9.0.post1 && \
    pip install gradio==5.9.1 && \
    pip install mauve-text==0.4.0 && \
    pip install evaluate==0.4.3 && \
    pip install torchmetrics==1.6.0 && \
    pip install nltk==3.9.1 && \
    pip install accelerate==1.2.1