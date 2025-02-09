FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/hailo-ai/hailo-rpi5-examples.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /hailo-rpi5-examples/. /repo && rm -rf /hailo-rpi5-examples/ && \
    rm -rf /hailo-rpi5-examples && \
    cd /repo && git checkout 82cfc8f61508e7d4ae733e3df7c8b93fa3c51ed6 && \
    pip install numpy==1.26.4 && \
    pip install setproctitle==1.3.4 && \
    pip install opencv-python==4.10.0.84
ENV PYTHONPATH=/repo