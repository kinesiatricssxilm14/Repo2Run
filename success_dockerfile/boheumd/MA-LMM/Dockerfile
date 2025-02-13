FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/boheumd/MA-LMM.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /MA-LMM/. /repo && rm -rf /MA-LMM/ && \
    rm -rf /MA-LMM && \
    cd /repo && git checkout ffe9fa9e89757e4433012029f19286c3c280ab1d && \
    pip install contexttimer==0.3.3 && \
    pip install decord==0.6.0 && \
    pip install einops==0.8.0 && \
    pip install fairscale==0.4.4 && \
    pip install ftfy==6.3.1 && \
    pip install iopath==0.1.10 && \
    pip install ipython==8.30.0 && \
    pip install omegaconf==2.3.0 && \
    pip install opencv-python-headless==4.5.5.64 && \
    pip install opendatasets==0.1.22 && \
    pip install packaging==24.2 && \
    pip install pandas==2.2.3 && \
    pip install plotly==5.24.1 && \
    pip install pre-commit==4.0.1 && \
    pip install pycocoevalcap==1.2 && \
    pip install pycocotools==2.0.8 && \
    pip install python-magic==0.4.27 && \
    pip install scikit-image==0.25.0 && \
    pip install sentencepiece==0.2.0 && \
    pip install spacy==3.8.3 && \
    pip install streamlit==1.41.1 && \
    pip install timm==0.4.12 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install tqdm==4.67.1 && \
    pip install transformers==4.47.1 && \
    pip install webdataset==0.2.100 && \
    pip install wheel==0.45.1 && \
    cd /repo && pip install -e . && \
    pip install numpy==1.24.0 -U --force-reinstall && \
    pip install opencv-python-headless==4.5.5.64 --force-reinstall && \
    pip uninstall -y opencv-python-headless && \
    pip install opencv-python-headless==4.5.5.64 && \
    pip uninstall -y numpy && \
    pip install numpy==1.21.2 opencv-python-headless==4.5.5.64 && \
    pip install numpy==1.24.0 && \
    pip uninstall -y pandas numpy && \
    pip install numpy==1.24.0 pandas==2.2.3 && \
    pip install numpy==1.24.0 -U --force-reinstall && \
    pip uninstall -y numpy opencv-python-headless && \
    pip install numpy==1.24.0 opencv-python-headless==4.5.5.64 && \
    pip uninstall -y numpy opencv-python-headless torch && \
    pip install numpy==1.24 opencv-python-headless==4.5.5.64 torch==2.5.1 && \
    mkdir -p /repo/docs/_static && \
    python -c "from PIL import Image; img = Image.new('RGB', (100, 100)); img.save('/repo/docs/_static/merlion.png')"