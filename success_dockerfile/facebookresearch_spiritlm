FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/facebookresearch/spiritlm.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /spiritlm/. /repo && rm -rf /spiritlm/ && \
    rm -rf /spiritlm && \
    cd /repo && git checkout 52fb2f4d585811450f192732a1c81760208b9fd0 && \
    pip install omegaconf==2.3.0 && \
    pip install librosa==0.10.2.post1 && \
    pip install local-attention==1.9.15 && \
    pip install encodec==0.1.1 && \
    pip install transformers==4.47.1 && \
    pip install fairscale==0.4.13 && \
    pip install sentencepiece==0.2.0 && \
    pip install pyarrow==18.1.0 && \
    pip install torchfcpe==0.0.4 && \
    pip install pytest==8.3.4 && \
    pip install pandas==2.2.3