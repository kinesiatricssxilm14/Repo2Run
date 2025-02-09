FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/McGill-NLP/webllama.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /webllama/. /repo && rm -rf /webllama/ && \
    rm -rf /webllama && \
    cd /repo && git checkout 696a7c3664fe6610b411a16d27010055874e2714 && \
    pip install weblinx==0.3.2 && \
    pip install lxml==5.3.0 && \
    pip install numpy==2.2.0 && \
    pip install weblinx[eval]==0.3.2 && \
    pip install streamlit==1.41.1 && \
    pip install sentence-transformers==3.3.1 && \
    pip install transformers==4.47.1 && \
    pip install playwright==1.49.1 && \
    pip install browsergym==0.13.3 && \
    cd /repo && pip install -e .