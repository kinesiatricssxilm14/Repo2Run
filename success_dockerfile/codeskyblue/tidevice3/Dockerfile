FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/codeskyblue/tidevice3.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /tidevice3/. /repo && rm -rf /tidevice3/ && \
    rm -rf /tidevice3 && \
    cd /repo && git checkout d83c345b2c5216c82baafb8e3c09574f8020ff00 && \
    cd /repo && poetry install
ENV PYTHONPATH=$PYTHONPATH:/repo