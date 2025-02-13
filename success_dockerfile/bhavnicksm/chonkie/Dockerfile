FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/bhavnicksm/chonkie.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /chonkie/. /repo && rm -rf /chonkie/ && \
    rm -rf /chonkie && \
    cd /repo && git checkout 990493550d4d16a95d3a5e20944d393cda591969 && \
    pip install -e /repo && \
    pip install numpy==2.2.0 && \
    pip install tokenizers==0.21.0 && \
    pip install datasets==3.2.0 && \
    pip install transformers==4.47.0 && \
    pip install model2vec==0.3.3 && \
    pip install sentence-transformers==3.3.1