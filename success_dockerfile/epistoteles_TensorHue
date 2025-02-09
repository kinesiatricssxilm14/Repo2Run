FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/epistoteles/TensorHue.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /TensorHue/. /repo && rm -rf /TensorHue/ && \
    rm -rf /TensorHue && \
    cd /repo && git checkout 1564fa78a8313586c981204145fd71fb501bbfae && \
    pip install numpy==2.0.2 && \
    pip install rich==13.9.4 && \
    pip install matplotlib==3.10.0 && \
    pip install pre-commit==4.0.1 && \
    pip install pylint==3.3.2 && \
    pip install torch==2.5.1 && \
    pip install tensorflow==2.18.0 && \
    pip install jax==0.4.38 && \
    pip install pillow==11.0.0 && \
    pip install tox==4.23.2 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install mypy==1.14.0 && \
    pip install flake8==7.1.1 && \
    pip install genbadge[all]==1.1.1
ENV PYTHONPATH=$PYTHONPATH:/repo/tensorhue
RUN cd /repo && pytest --collect-only -q