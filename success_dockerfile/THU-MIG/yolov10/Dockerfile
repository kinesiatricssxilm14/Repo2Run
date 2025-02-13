FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/THU-MIG/yolov10.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /yolov10/. /repo && rm -rf /yolov10/ && \
    rm -rf /yolov10 && \
    cd /repo && git checkout 6fbaf42b23f6709f4e34a51430587673e70e151d && \
    pip install torch==2.0.1 && \
    pip install torchvision==0.15.2 && \
    pip install onnx==1.14.0 && \
    pip install onnxruntime==1.15.1 && \
    pip install pycocotools==2.0.7 && \
    pip install PyYAML==6.0.1 && \
    pip install scipy==1.13.0 && \
    pip install onnxslim==0.1.31 && \
    pip install onnxruntime-gpu==1.18.0 && \
    pip install gradio==4.31.5 && \
    pip install opencv-python==4.9.0.80 && \
    pip install psutil==5.9.8 && \
    pip install py-cpuinfo==9.0.0 && \
    pip install huggingface-hub==0.23.2 && \
    pip install safetensors==0.4.3 && \
    pip install -e /repo && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1-mesa-glx && \
    pip install shapely==2.0.6 && \
    pip install sahi==0.11.20 && \
    pip install sahi[all]==0.11.20 && \
    mkdir -p /repo/examples/backup && \
    mv /repo/examples/YOLOv8-OpenCV-ONNX-Python/main.py /repo/examples/backup/ && \
    mv /repo/examples/YOLOv8-OpenCV-int8-tflite-Python/main.py /repo/examples/backup/ && \
    mv /repo/examples/YOLOv8-SAHI-Inference-Video/yolov8_sahi.py /repo/examples/backup/ && \
    mv /repo/examples/YOLOv8-Segmentation-ONNXRuntime-Python/main.py /repo/examples/backup/ && \
    rm -rf /repo/examples/backup