FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Adibvafa/CodonTransformer.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /CodonTransformer/. /repo && rm -rf /CodonTransformer/ && \
    rm -rf /CodonTransformer && \
    cd /repo && git checkout 2842ef05444d6901cb4034aab1b3153db3ee4926 && \
    pip install biopython==1.84 && \
    pip install CAI-PyPI==2.0.1 && \
    pip install ipywidgets==8.1.5 && \
    pip install numpy==2.2.1 && \
    pip install onnxruntime==1.20.1 && \
    pip install pandas==2.2.3 && \
    pip install python_codon_tables==0.1.12 && \
    pip install pytorch_lightning==2.5.0.post0 && \
    pip install scikit-learn==1.6.0 && \
    pip install scipy==1.15.0 && \
    pip install setuptools==75.7.0 && \
    pip install torch==2.5.1 && \
    pip install tqdm==4.67.1 && \
    pip install transformers==4.47.1
RUN cd /repo && pytest --collect-only -q