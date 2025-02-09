FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Lightning-AI/litdata.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /litdata/. /repo && rm -rf /litdata/ && \
    rm -rf /litdata && \
    cd /repo && git checkout 0a97def7eaaa8c38072da62e470cde8dfb7d3932 && \
    pip install torch==2.5.1 && \
    pip install lightning-utilities==0.11.9 && \
    pip install filelock==3.16.1 && \
    pip install numpy==2.2.0 && \
    pip install boto3==1.35.84 && \
    pip install requests==2.32.3 && \
    pip install tifffile==2024.12.12 && \
    cd /repo && pip install -e . && \
    pip install joblib==1.4.2 && \
    pip install names==0.3.0 && \
    pip install lightning==2.4.0 && \
    pip install cryptography==44.0.0 && \
    pip install lightning_sdk==0.1.41 && \
    pip install pillow==11.0.0 && \
    pip install scikit-learn==1.6.0 && \
    pip install torchvision==0.20.1 && \
    pip install pandas==2.2.3 && \
    pip install pyarrow==18.1.0 && \
    pip install transformers==4.47.1 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch"
ENV AWS_ACCESS_KEY_ID='dummy-access-key'
ENV AWS_SECRET_ACCESS_KEY='dummy-secret-key'
ENV AWS_DEFAULT_REGION='us-east-1'
RUN pip install fpdf==1.7.2 && \
    pip install pdf2image==1.17.0