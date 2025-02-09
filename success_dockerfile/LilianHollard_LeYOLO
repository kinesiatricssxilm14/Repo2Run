FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/LilianHollard/LeYOLO.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /LeYOLO/. /repo && rm -rf /LeYOLO/ && \
    rm -rf /LeYOLO && \
    cd /repo && git checkout 872841b15fd5ee3296a9c844bcbfb8d0b9745cee && \
    pip install -e /repo && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1 && \
    pip install huggingface_hub==0.27.0