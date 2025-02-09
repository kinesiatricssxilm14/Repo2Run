FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/NVlabs/Sana.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Sana/. /repo && rm -rf /Sana/ && \
    rm -rf /Sana && \
    cd /repo && git checkout 41dcbe92671682216d357c385c0d3d7dab0e8e55 && \
    pip install pip==24.3.1 -U && \
    pip install xformers==0.0.27.post2 --index-url https://download.pytorch.org/whl/cu121 -U && \
    pip install -e /repo
RUN cd /repo && poetry run pytest --collect-only -q