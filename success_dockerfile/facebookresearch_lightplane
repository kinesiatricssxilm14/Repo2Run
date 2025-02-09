FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/facebookresearch/lightplane.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /lightplane/. /repo && rm -rf /lightplane/ && \
    rm -rf /lightplane && \
    cd /repo && git checkout 34fe6c6392028b2993613d4ceeeeec2abadbc1c9 && \
    cd /repo && pip install -e . && \
    pip install torch==2.5.1
ENV PYTHONPATH=/repo/tests
RUN pip install numpy==2.2.0
ENV PYTHONPATH=/repo/tests
RUN pip install plotly==5.24.1
ENV PYTHONPATH=/repo/tests