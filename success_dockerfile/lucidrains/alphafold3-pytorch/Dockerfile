FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lucidrains/alphafold3-pytorch.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /alphafold3-pytorch/. /repo && rm -rf /alphafold3-pytorch/ && \
    rm -rf /alphafold3-pytorch && \
    cd /repo && git checkout 49f7c967e8586b9f57bdb95e82068fabda815689 && \
    pip install hatch==1.14.0 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    pip install adam-atan2-pytorch==0.1.18 && \
    pip install awscliv2==2.3.1 && \
    pip install beartype==0.19.0 && \
    pip install biopython==1.84 && \
    pip install cachetools==5.5.0 && \
    pip install click==8.1.7 && \
    pip install CoLT5-attention==0.11.1 && \
    pip install einops==0.8.0 && \
    pip install einx==0.3.0 && \
    pip install ema-pytorch==0.7.7 && \
    pip install environs==11.2.1 && \
    pip install lion-pytorch==0.2.3 && \
    pip install joblib==1.4.2 && \
    pip install gemmi==0.6.7 && \
    pip install fair-esm==2.0.0 && \
    pip install fastapi==0.115.6 && \
    pip install frame-averaging-pytorch==0.1.2 && \
    pip install gradio==5.9.1 && \
    pip install gradio_molecule3d==0.0.6 && \
    pip install huggingface_hub==0.27.0 && \
    pip install jaxtyping==0.2.36 && \
    pip install lightning==2.5.0 && \
    pip install multimolecule==0.0.6 && \
    pip install nimporter==1.1.0 && \
    pip install numpy==1.26.4 && \
    pip install polars==1.17.1 && \
    pip install pdbeccdutils==0.8.5 && \
    pip install pydantic==2.10.4 && \
    pip install pyyaml==6.0.2 && \
    pip install rdkit==2023.9.6 && \
    pip install retrying==1.3.4 && \
    pip install scikit-learn==1.6.0 && \
    pip install scipy==1.13.1 && \
    pip install sentencepiece==0.2.0 && \
    pip install sh==2.1.0 && \
    pip install shortuuid==1.0.13 && \
    pip install tensorboard==2.18.0 && \
    pip install taylor-series-linear-attention==0.1.12 && \
    pip install torchtyping==0.1.5 && \
    pip install timeout_decorator==0.5.0 && \
    pip install torch_geometric==2.6.1 && \
    pip install torch==2.5.1 && \
    pip install tqdm==4.67.1 && \
    pip install transformers[torch]==4.47.1 && \
    pip install loguru==0.7.3 && \
    pip install -e /repo