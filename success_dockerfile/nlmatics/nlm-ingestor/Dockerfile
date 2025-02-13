FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/nlmatics/nlm-ingestor.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /nlm-ingestor/. /repo && rm -rf /nlm-ingestor/ && \
    rm -rf /nlm-ingestor && \
    cd /repo && git checkout c725429dbf46d6e633965ccbc4c24c14c97c6efc && \
    cd /repo && pip install -e . && \
    python -m nltk.downloader punkt
ENV PYTHONPATH=/repo
RUN python -m nltk.downloader stopwords && \
    python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=/repo
ENV PYTHONPATH=/repo:/repo/nlm_ingestor
RUN cd /repo && pytest --collect-only -q