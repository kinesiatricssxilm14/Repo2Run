FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/AnswerDotAI/byaldi.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /byaldi/. /repo && rm -rf /byaldi/ && \
    rm -rf /byaldi && \
    cd /repo && git checkout 4583c0732fac06cca5624c53a539a7785d226ce8 && \
    pip install ml-dtypes==0.5.1 && \
    pip install mteb==1.6.35 && \
    pip install ninja==1.11.1.3 && \
    pip install pdf2image==1.17.0 && \
    pip install srsly==2.5.0 && \
    pip install torch==2.5.1 && \
    pip install transformers==4.46.3 && \
    pip install pytest==8.3.4 && \
    pip install ruff==0.8.6 && \
    pip install colpali-engine==0.3.5 && \
    pip install -e /repo
RUN cd /repo && pytest --collect-only -q