FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/google-deepmind/treescope.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /treescope/. /repo && rm -rf /treescope/ && \
    rm -rf /treescope && \
    cd /repo && git checkout dac18b2ace0badf70b6fb887170bed4c6424bf06 && \
    pip install numpy==2.2.0 && \
    pip install absl-py==2.1.0 && \
    pip install jax==0.4.38 && \
    pip install pytest==8.3.4 && \
    pip install torch==2.5.1 && \
    pip install ipython==8.30.0 && \
    pip install palettable==3.3.3 && \
    pip install pylint==3.3.2 && \
    pip install pyink==24.10.0 && \
    pip install jupyter==1.1.1 && \
    pip install pytype==2024.10.11 && \
    pip install sphinx-book-theme==1.1.3 && \
    pip install sphinxcontrib-katex==0.9.10 && \
    pip install myst-nb==1.1.2 && \
    pip install myst-parser==4.0.0 && \
    pip install matplotlib==3.10.0 && \
    pip install packaging==24.1 && \
    pip install pandas==2.2.2 && \
    pip install plotly==5.22.0 && \
    pip install sphinx_contributors==0.2.7 && \
    pip install sphinx-hoverxref==1.4.2 && \
    pip install penzai==0.2.4
ENV PYTHONPATH=/repo