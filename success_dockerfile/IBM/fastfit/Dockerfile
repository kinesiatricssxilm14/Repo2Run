FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/IBM/fastfit.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fastfit/. /repo && rm -rf /fastfit/ && \
    rm -rf /fastfit && \
    cd /repo && git checkout 3966113090ec7e8732be3bb48ca6b775d6c203c9 && \
    pip install torch==2.5.1 && \
    pip install transformers[torch]==4.47.1 && \
    pip install scikit-learn==1.6.0 && \
    pip install datasets==3.2.0 && \
    pip install evaluate==0.4.3 && \
    cd /repo && pip install -e .