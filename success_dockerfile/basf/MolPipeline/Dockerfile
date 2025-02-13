FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/basf/MolPipeline.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /MolPipeline/. /repo && rm -rf /MolPipeline/ && \
    rm -rf /MolPipeline && \
    cd /repo && git checkout 2f9baee03f82408991362f0719ff22ff9e4e2524 && \
    pip install chemprop==2.0.4 && \
    pip install loguru==0.7.3 && \
    pip show chemprop && \
    pip install torch==2.5.1 && \
    pip install chemprop==2.0.4