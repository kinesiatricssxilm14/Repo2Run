FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/NVlabs/nvTorchCam.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /nvTorchCam/. /repo && rm -rf /nvTorchCam/ && \
    rm -rf /nvTorchCam && \
    cd /repo && git checkout cc27be07a2e19972c43a3342571eb86f39135a6b && \
    cd /repo && pip install -e . && \
    pip install opencv-python==4.10.0.84 && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1-mesa-glx