FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/tobiasfshr/map4d.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /map4d/. /repo && rm -rf /map4d/ && \
    rm -rf /map4d && \
    cd /repo && git checkout 0b8bcd3302e9036eb74420d6730af8dc5556f6d7 && \
    pip install plyfile==1.1 && \
    pip install pyarrow==18.1.0 && \
    pip install utm==0.7.0 && \
    pip install gsplat==1.4.0 && \
    pip install typeguard==2.13.3 && \
    pip install nerfstudio==1.1.5 && \
    pip install git+https://github.com/richzhang/PerceptualSimilarity && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1
ENV PYTHONPATH=$PYTHONPATH:/repo/src