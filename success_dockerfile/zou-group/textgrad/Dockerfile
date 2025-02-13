FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/zou-group/textgrad.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /textgrad/. /repo && rm -rf /textgrad/ && \
    rm -rf /textgrad && \
    cd /repo && git checkout b2dc68e992ad876cfacdb8ebb7f73d8865a29544 && \
    pip install openai==1.59.5 && \
    pip install tenacity==9.0.0 && \
    pip install python-dotenv==1.0.1 && \
    pip install pandas==2.2.3 && \
    pip install platformdirs==4.3.6 && \
    pip install datasets==3.2.0 && \
    pip install diskcache==5.6.3 && \
    pip install graphviz==0.20.3 && \
    pip install gdown==5.2.0 && \
    pip install litellm==1.57.3 && \
    pip install pillow==11.1.0 && \
    pip install httpx==0.27.2 && \
    pip install ipython==8.31.0
RUN cd /repo && pytest --collect-only -q