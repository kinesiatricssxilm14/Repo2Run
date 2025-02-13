FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/openpsi-project/ReaLHF.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ReaLHF/. /repo && rm -rf /ReaLHF/ && \
    rm -rf /ReaLHF && \
    cd /repo && git checkout 62d9cdfb0715431f21455d2d9e0535e1c1980994 && \
    pip install sphinx-nefertiti==0.7.3 && \
    pip install sphinx==8.1.3 && \
    pip install build==1.2.2.post1 && \
    pip install wheel==0.45.1 && \
    pip install distro-info==1.0 && \
    pip install python-debian==0.1.49 && \
    pip install huggingface_hub==0.27.0 && \
    pip install datasets==3.2.0 && \
    pip install accelerate==1.2.1 && \
    pip install ninja==1.11.1.3 && \
    pip install matplotlib==3.10.0 && \
    pip install ipython==8.30.0 && \
    pip install megatron_core==0.6.0 && \
    pip install deepspeed==0.14.0 && \
    pip install h5py==3.12.1 && \
    pip install nltk==3.9.1 && \
    pip install sentencepiece==0.2.0 && \
    pip install wandb==0.19.1 && \
    pip install tensorboardx==2.6.2.2 && \
    pip install blosc==1.11.2 && \
    pip install colorama==0.4.6 && \
    pip install colorlog==6.9.0 && \
    pip install einops==0.8.0 && \
    pip install hydra-core==1.3.2 && \
    pip install numba==0.60.0 && \
    pip install omegaconf==2.3.0 && \
    pip install packaging==24.2 && \
    pip install pandas==2.2.3 && \
    pip install pybind11==2.10.0 && \
    pip install numpy==1.26.4 && \
    pip install psutil==6.1.0 && \
    pip install pynvml==11.5.3 && \
    pip install pytest==8.3.4 && \
    pip install PyYAML==6.0.2 && \
    pip install pyzmq==26.2.0 && \
    pip install ray==2.40.0 && \
    pip install redis==5.2.1 && \
    pip install scipy==1.14.1 && \
    pip install seaborn==0.13.2 && \
    pip install setuptools==65.5.1 && \
    pip install tqdm==4.67.1 && \
    pip install transformers==4.42.3 && \
    pip install networkx==3.3 && \
    pip install tabulate==0.9.0 && \
    pip install aiofiles==24.1.0
ENV PYTHONPATH=/repo
RUN pip show torch deepspeed && \
    pip install torch==1.13.0 && \
    pip install pybind11==2.10.0 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    apt-get update -qq && \
    apt-get install -y -qq ninja-build cmake && \
    apt-get update -qq && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    pip check && \
    apt-get install -y -qq build-essential && \
    python -m torch.utils.cpp_extension --show
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q