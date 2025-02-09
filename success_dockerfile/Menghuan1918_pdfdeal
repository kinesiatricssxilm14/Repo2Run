FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Menghuan1918/pdfdeal.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /pdfdeal/. /repo && rm -rf /pdfdeal/ && \
    rm -rf /pdfdeal && \
    cd /repo && git checkout e081998afbc26c51f175e09882075c8e82316dc7 && \
    pip install pypdf==5.1.0 && \
    pip install pytest==8.3.4 && \
    pip install emoji==2.14.0 && \
    pip install pillow==11.0.0 && \
    pip install reportlab==4.2.5 && \
    pip install oss2==2.19.1 && \
    pip install boto3==1.35.82 && \
    pip install minio==7.2.12 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install httpx==0.28.1
ENV PYTHONPATH=$PYTHONPATH:/repo/src