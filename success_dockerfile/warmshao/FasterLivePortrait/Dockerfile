FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/warmshao/FasterLivePortrait.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /FasterLivePortrait/. /repo && rm -rf /FasterLivePortrait/ && \
    rm -rf /FasterLivePortrait && \
    cd /repo && git checkout 6aa8104b03499ebe2a881c8fbaf55ff628235f4f && \
    pip install ffmpeg-python==0.2.0 && \
    pip install omegaconf==2.3.0 && \
    pip install onnx==1.17.0 && \
    pip install numpy==1.26.4 && \
    pip install opencv-python==4.10.0.84 && \
    pip install gradio==5.9.1 && \
    pip install scikit-image==0.25.0 && \
    pip install insightface==0.7.3 && \
    pip install huggingface_hub[cli]==0.27.0 && \
    pip install mediapipe==0.10.20 && \
    pip install torchgeometry==0.1.2 && \
    apt-get update -qq && \
    apt-cache search cuda | grep dev && \
    apt-get update -qq && \
    apt-get install -y -qq software-properties-common && \
    apt-get update -qq