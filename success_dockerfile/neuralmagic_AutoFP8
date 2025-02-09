FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/neuralmagic/AutoFP8.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /AutoFP8/. /repo && rm -rf /AutoFP8/ && \
    rm -rf /AutoFP8 && \
    cd /repo && git checkout e9446102c6a9ccf148e1ba661185c60056e3ce80 && \
    pip install torch==2.5.1 && \
    pip install transformers==4.47.1 && \
    pip install datasets==3.2.0 && \
    pip install accelerate==1.2.1 && \
    pip install tqdm==4.67.1
ENV PYTHONPATH=$PYTHONPATH:/repo