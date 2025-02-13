FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/kotaro-kinoshita/yomitoku.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /yomitoku/. /repo && rm -rf /yomitoku/ && \
    rm -rf /yomitoku && \
    cd /repo && git checkout 71c85bc77a5ed238f382f51adeb208ecef4cefb4 && \
    pip install hatch==1.14.0 && \
    pip install huggingface-hub==0.27.0 && \
    pip install lxml==5.3.0 && \
    pip install omegaconf==2.3.0 && \
    pip install opencv-python==4.10.0.84 && \
    pip install pyclipper==1.3.0.post6 && \
    pip install pydantic==2.10.3 && \
    pip install shapely==2.0.6 && \
    pip install timm==1.0.12 && \
    pip install torchvision==0.20.1 && \
    pip install torch==2.5.1 && \
    pip install pypdfium2==4.30.0 && \
    pip install mkdocs-material==9.5.49 && \
    pip install mkdocs-static-i18n==1.2.3 && \
    pip install mkdocs==1.6.1 && \
    pip install plantuml-markdown==3.10.4 && \
    pip install pygments==2.18.0 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest==8.3.4 && \
    pip install ruff==0.8.3
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN apt-get update -qq && \
    apt-get install -y -qq libgl1-mesa-glx
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install -e /repo
ENV PYTHONPATH=$PYTHONPATH:/repo/src