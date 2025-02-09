FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/RapidAI/RapidLayout.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /RapidLayout/. /repo && rm -rf /RapidLayout/ && \
    rm -rf /RapidLayout && \
    cd /repo && git checkout 8e9677386ecec315c466e840c0b654f7eab85b69 && \
    pip install onnxruntime==1.20.1 && \
    pip install opencv_python==4.10.0.84 && \
    pip install numpy==1.26.4 && \
    pip install Pillow==11.0.0 && \
    pip install tqdm==4.67.1 && \
    pip install requests==2.32.3 && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1-mesa-glx