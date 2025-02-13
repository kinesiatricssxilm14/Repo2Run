FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/shawntan/scattermoe.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /scattermoe/. /repo && rm -rf /scattermoe/ && \
    rm -rf /scattermoe && \
    cd /repo && git checkout 63b76a2f5f28c052fb4cd7c34479a54158354052 && \
    cd /repo && pip install -e .