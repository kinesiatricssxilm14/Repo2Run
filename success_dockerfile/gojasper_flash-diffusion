FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/gojasper/flash-diffusion.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /flash-diffusion/. /repo && rm -rf /flash-diffusion/ && \
    rm -rf /flash-diffusion && \
    cd /repo && git checkout 48e3bcd654d98be3891e1e02cf215ae6218f924b && \
    cd /repo && pip install -e . && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1-mesa-glx && \
    pip install diffusers==0.32.1 && \
    pip show opencv-python controlnet_aux && \
    pip install numpy==1.25.0 -U && \
    pip install opencv-python==4.5.5.64 && \
    pip install controlnet-aux==0.0.6 && \
    pip install opencv-python==4.9.0.80 controlnet-aux==0.0.7 && \
    pip install opencv-python-headless==4.10.0.84 && \
    pip install numpy==1.25.0
RUN cd /repo && pytest --collect-only -q