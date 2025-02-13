FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/block/goose.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /goose/. /repo && rm -rf /goose/ && \
    rm -rf /goose && \
    cd /repo && git checkout c497a5555848d053dd8b486bce1371ba6d01d06c && \
    pip install attrs==24.3.0 && \
    pip install rich==13.9.4 && \
    pip install ruamel-yaml==0.18.6 && \
    pip install click==8.1.7 && \
    pip install prompt-toolkit==3.0.48 && \
    pip install keyring==25.5.0 && \
    pip install langfuse==2.57.0 && \
    pip install selenium==4.27.1 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install google-workspace==0.20.3 && \
    pip install ai-exchange==0.9.9
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install ai-exchange==0.9.9 && \
    pip install pyyaml==6.0.2
ENV PYTHONPATH=$PYTHONPATH:/repo/packages/exchange/src
ENV PYTHONPATH=$PYTHONPATH:/repo/packages/exchange/src:/repo/src
RUN pip install pyshadow==0.0.3
ENV PYTHONPATH=/repo/packages/exchange/src:/repo/src