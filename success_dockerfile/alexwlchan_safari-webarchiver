FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/alexwlchan/safari-webarchiver.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /safari-webarchiver/. /repo && rm -rf /safari-webarchiver/ && \
    rm -rf /safari-webarchiver && \
    cd /repo && git checkout 0e4974d4af6ab28da9178b02f4a5067855ddf91d && \
    pip install execnet==2.1.1 && \
    pip install iniconfig==2.0.0 && \
    pip install markupsafe==2.1.5 && \
    pip install packaging==24.0 && \
    pip install pluggy==1.5.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-httpserver==1.1.0 && \
    pip install pytest-xdist==3.6.1 && \
    pip install werkzeug==3.0.3