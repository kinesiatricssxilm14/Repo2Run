FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/TorchJD/torchjd.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /torchjd/. /repo && rm -rf /torchjd/ && \
    rm -rf /torchjd && \
    cd /repo && git checkout 1eaafee3cf386ac17198b7864a8146d5d803e0be && \
    pip install torch==2.5.1 && \
    pip install numpy==2.2.0 && \
    pip install qpsolvers==4.4.0 && \
    pip install cvxpy==1.6.0 && \
    pip install ecos==2.0.14 && \
    pip install quadprog==0.1.13 && \
    pip install pre-commit==4.0.1 && \
    pip install sphinx==8.1.3 && \
    pip install tomli==2.2.1 && \
    pip install sphinx-autodoc-typehints==2.5.0 && \
    pip install myst-parser==4.0.0 && \
    pip install sphinx-design==0.6.1 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install lightning==2.4.0 && \
    pip install plotly==5.24.1 && \
    pip install dash==2.18.2 && \
    pip install kaleido==0.2.1 && \
    pip install furo==2024.8.6 && \
    pip install -e /repo