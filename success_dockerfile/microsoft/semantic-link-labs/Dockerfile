FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/microsoft/semantic-link-labs.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /semantic-link-labs/. /repo && rm -rf /semantic-link-labs/ && \
    rm -rf /semantic-link-labs && \
    cd /repo && git checkout 8e37efd7333f43e78d3a0fc330155d4abc857567 && \
    pip install semantic-link-sempy==0.8.3 && \
    pip install azure-identity==1.7.1 && \
    pip install azure-storage-blob==12.24.0 && \
    pip install pandas-stubs==2.2.3.241126 && \
    pip install types-tqdm==4.67.0.20241119 && \
    pip install pandas==2.2.3
ENV PYTHONPATH=/repo/src
RUN pip install pyspark==3.5.3
ENV PYTHONPATH=/repo/src
RUN pip install ipython==8.30.0
ENV PYTHONPATH=/repo/src
RUN pip install anytree==2.12.1
ENV PYTHONPATH=/repo/src
RUN pip install ipywidgets==8.1.5
ENV PYTHONPATH=/repo/src
RUN cd /repo && pytest --collect-only -q