FROM python:3.12
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/getludic/ludic.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ludic/. /repo && rm -rf /ludic/ && \
    rm -rf /ludic && \
    cd /repo && git checkout a6db96340602a4bd8a507e70d3e8321b1a1bcde1 && \
    pip install hatch==1.13.0 && \
    cd /repo && hatch env create && \
    pip install django==5.1.4 && \
    pip install typing_extensions==4.12.2 && \
    pip install starlette==0.41.3 && \
    pip install typeguard==4.4.1