FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/alexmolas/microsearch.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /microsearch/. /repo && rm -rf /microsearch/ && \
    rm -rf /microsearch && \
    cd /repo && git checkout 632ff20749f30b972df84a4ef544b751a18155d5 && \
    pip install aiohttp==3.9.1 && \
    pip install beautifulsoup4==4.12.2 && \
    pip install fastapi==0.108.0 && \
    pip install feedparser==6.0.11 && \
    pip install Jinja2==3.1.3 && \
    pip install pandas==2.1.4 && \
    pip install pyarrow==15.0.0 && \
    pip install uvicorn==0.25.0
ENV PYTHONPATH=/repo/src