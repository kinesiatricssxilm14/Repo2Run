FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/NVIDIA/NeMo-Skills.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /NeMo-Skills/. /repo && rm -rf /NeMo-Skills/ && \
    rm -rf /NeMo-Skills && \
    cd /repo && git checkout 5591f399b3263d349c6f5f5d7d635c3fb0b744e6 && \
    pip install bs4==0.0.2 && \
    pip install huggingface_hub==0.27.0 && \
    pip install hydra-core==1.3.2 && \
    pip install numpy==1.26.0 && \
    pip install openai==1.57.4 && \
    pip install pyyaml==6.0.2 && \
    pip install rank_bm25==0.2.2 && \
    pip install requests==2.32.3 && \
    pip install scikit-learn==1.6.0 && \
    pip install sympy==1.13.3 && \
    pip install tqdm==4.67.1 && \
    pip install transformers==4.47.0 && \
    pip install typer==0.15.1 && \
    pip install wandb==0.19.1 && \
    pip install datasets==3.2.0 && \
    pip install git+https://github.com/evalplus/evalplus@c91370f && \
    pip install git+https://github.com/NVIDIA/NeMo-Run.git && \
    pip install git+https://github.com/NVIDIA/NeMo-speech-data-processor.git
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install pydantic==1.10.0 && \
    pip uninstall -q wandb -y && \
    pip install wandb==0.19.1 && \
    pip install pydantic==1.10.7
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install pydantic==1.10.7 fastapi==0.115.6 uvicorn==0.34.0
ENV PYTHONPATH=/repo/nemo_skills:$PYTHONPATH
RUN pip install srsly==2.5.0 && \
    pip install selenium==4.27.1 && \
    pip install webdriver_manager==4.0.2 && \
    pip install git+https://github.com/NVIDIA/NeMo-speech-data-processor.git
ENV PYTHONPATH=/repo:/repo/nemo_skills:$PYTHONPATH