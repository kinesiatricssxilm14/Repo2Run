FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/openai/mle-bench.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mle-bench/. /repo && rm -rf /mle-bench/ && \
    rm -rf /mle-bench && \
    cd /repo && git checkout 51ec2b6789a5df0f902537e5b066dd0f6b8a6c2f && \
    cd /repo && curl -sSL https://install.python-poetry.org | python3 - && \
    pip install appdirs==1.4.4 docker==7.1.0 fastparquet==2024.11.0 kaggle==1.6.17 Levenshtein==0.26.1 openai==1.57.4 pandas==2.2.3 pyyaml==6.0.2 py7zr==0.22.0 scikit-learn==1.6.0 tensorflow==2.18.0 pillow==11.0.0 python-dotenv==1.0.1 aiohttp==3.11.10 tenacity==9.0.0 nbformat==5.10.4 nbconvert==7.16.4 ipython==8.30.0 pymongo==4.10.1 pycocotools==2.0.8 diskcache==5.6.3 pyquaternion==0.9.9 shapely==2.0.6