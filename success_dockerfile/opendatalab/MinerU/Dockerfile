FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/opendatalab/MinerU.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /MinerU/. /repo && rm -rf /MinerU/ && \
    rm -rf /MinerU && \
    cd /repo && git checkout 391a99860dba33a19abf6df90234bdcee554b32a && \
    pip install boto3==1.35.81 && \
    pip install Brotli==1.1.0 && \
    pip install click==8.1.7 && \
    pip install fast-langdetect==0.2.0 && \
    pip install loguru==0.7.3 && \
    pip install numpy==1.26.4 && \
    pip install pydantic==2.10.3 && \
    pip install PyMuPDF==1.25.1 && \
    pip install scikit-learn==1.6.0 && \
    pip install torch==2.5.1 && \
    pip install transformers==4.42.4 && \
    pip install pdfminer.six==20231228 && \
    pip install python-levenshtein==0.26.1 && \
    pip install pillow==11.0.0
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install lxml==5.3.0 && \
    pip install paddlepaddle==2.6.2
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install opencv-python==4.10.0.84
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN apt-get update -qq && \
    apt-get install libgl1 -y -qq
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install doclayout-yolo==0.0.2 && \
    pip install rapid-table==0.3.0
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install pycocotools==2.0.8
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install torch==2.5.1 && \
    pip install git+https://github.com/facebookresearch/detectron2.git
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install timm==0.9.16
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install ultralytics==8.3.50
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install unimernet==0.2.2
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install paddleocr==2.9.1
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install rapidocr_paddle==1.4.4
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install struct_eqtable==0.3.3
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install nltk==3.9.1
ENV PYTHONPATH=/repo:$PYTHONPATH
ENV GITHUB_WORKSPACE=/repo
ENV PYTHONPATH=/repo:$PYTHONPATH