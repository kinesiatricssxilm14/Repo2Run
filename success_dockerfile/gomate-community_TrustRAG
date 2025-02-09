FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/gomate-community/TrustRAG.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /TrustRAG/. /repo && rm -rf /TrustRAG/ && \
    rm -rf /TrustRAG && \
    cd /repo && git checkout 1334c44a05a32ccc3fcd0eb9f1111eee05c65da6 && \
    pip install tqdm==4.67.1 && \
    pip install hyperopt==0.2.7 && \
    pip install h5py==3.12.1 && \
    pip install coverage==7.6.9 && \
    pip install codecov==2.1.13 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install flake8==7.1.1 && \
    pip install flake8_docstrings==1.7.0 && \
    pip install pydocstyle==6.3.0 && \
    pip install openai==1.57.4 && \
    pip install datasets==2.19.0 && \
    pip install langchain==0.3.12 && \
    pip install langchain-core==0.3.25 && \
    pip install langchain-text-splitters==0.3.3 && \
    pip install langchain-huggingface==0.1.2 && \
    pip install langchain-openai==0.2.12 && \
    pip install langsmith==0.2.3 && \
    pip install transformers==4.44.2 && \
    pip install pandas==2.2.3 && \
    pip install nltk==3.9.1 && \
    pip install sentencepiece==0.2.0 && \
    pip install PyPDF2==3.0.1 && \
    pip install html2text==2024.2.26 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install faiss-cpu==1.9.0.post1 && \
    pip install umap-learn==0.5.7 && \
    pip install sentence_transformers==3.3.1 && \
    pip install threadpoolctl==3.5.0 && \
    pip install PyMuPDF==1.25.1 && \
    pip install hanziconv==0.3.2 && \
    pip install datrie==0.8.2 && \
    pip install xpinyin==0.7.6 && \
    pip install python-pptx==1.0.2 && \
    pip install pdfplumber==0.11.4 && \
    pip install readability==0.3.1 && \
    pip install html_text==0.6.2 && \
    pip install python-docx==1.1.2 && \
    pip install tortoise==0.1.1 && \
    pip install python-magic==0.4.27 && \
    pip install gradio==5.9.1 && \
    pip install loguru==0.7.3 && \
    pip install xgboost==2.1.3 && \
    pip install bm25s==0.2.5 && \
    pip install jieba==0.42.1 && \
    pip install accelerate==1.2.1 && \
    pip install FlagEmbedding==1.3.3 && \
    pip install chardet==5.2.0 && \
    pip install openpyxl==3.1.5 && \
    pip install protobuf==5.29.1 && \
    pip install peft==0.14.0 && \
    pip install minio==7.2.12 && \
    pip install bson==0.5.10 && \
    pip install elasticsearch==8.17.0 && \
    pip install pymongo==4.8.0
ENV PYTHONPATH=/repo
RUN python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q