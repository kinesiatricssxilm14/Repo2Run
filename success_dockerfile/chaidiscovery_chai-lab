FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/chaidiscovery/chai-lab.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /chai-lab/. /repo && rm -rf /chai-lab/ && \
    rm -rf /chai-lab && \
    cd /repo && git checkout b6e7fa1a9135acc2ce6f4a5dfdd6fe435a3b216f && \
    pip install ruff==0.6.3 && \
    pip install mypy==1.13.0 && \
    pip install pytest==8.3.4 && \
    pip install pre-commit==4.0.1 && \
    pip install pandas-stubs==2.2.3.241126 && \
    pip install types-pyyaml==6.0.12.20240917 && \
    pip install types-tqdm==4.67.0.20241119 && \
    pip install typing-extensions==4.12.2 && \
    pip install types-requests==2.32.0.20241016 && \
    pip install typer==0.15.1 && \
    pip install ipykernel==6.29.5 && \
    pip install matplotlib==3.10.0 && \
    pip install tqdm==4.67.1 && \
    pip install gemmi==0.6.7 && \
    pip install rdkit==2023.9.5 && \
    pip install biopython==1.84 && \
    pip install antipickle==0.2.0 && \
    pip install tmtools==0.2.0 && \
    pip install modelcif==1.2 && \
    pip install numpy==1.26.4 && \
    pip install pandas[parquet,gcp,aws]==2.2.3 && \
    pip install pandera==0.21.1 && \
    pip install numba==0.60.0 && \
    pip install einops==0.8.0 && \
    pip install jaxtyping==0.2.36 && \
    pip install beartype==0.19.0 && \
    pip install torch==2.3.1 && \
    pip install transformers==4.47.0