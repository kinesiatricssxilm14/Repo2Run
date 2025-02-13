FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/dreadnode/rigging.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /rigging/. /repo && rm -rf /rigging/ && \
    rm -rf /rigging && \
    cd /repo && git checkout 1d12095c611d0f7c42230143d42723f80294282f && \
    cd /repo && poetry install && \
    pip install elasticsearch==8.16.0 && \
    pip install pandas==2.2.3 && \
    pip install loguru==0.7.2 && \
    pip install pydantic==2.10.3 && \
    pip install xmltodict==0.14.2 && \
    pip install pydantic_xml==2.14.1 && \
    pip install litellm==1.53.7 && \
    pip install colorama==0.4.6