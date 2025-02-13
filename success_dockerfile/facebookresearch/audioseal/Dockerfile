FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/facebookresearch/audioseal.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /audioseal/. /repo && rm -rf /audioseal/ && \
    rm -rf /audioseal && \
    cd /repo && git checkout ea10f5da2bb4431a4efee9452ed35db6ffaf83cf && \
    pip install numpy==2.2.0 && \
    pip install omegaconf==2.3.0 && \
    pip install julius==0.2.7 && \
    pip install torch==2.5.1 && \
    pip install fire==0.7.0 && \
    pip install torchaudio==2.5.1 && \
    pip install soundfile==0.12.1 && \
    pip install pytest==8.3.4 && \
    pip install mypy==1.13.0 && \
    pip install black==24.10.0 && \
    pip install isort==5.13.2 && \
    pip install flake8==7.1.1 && \
    pip install pre-commit==4.0.1 && \
    pip install huggingface_hub==0.27.0
ENV PYTHONPATH=$PYTHONPATH:/repo/src