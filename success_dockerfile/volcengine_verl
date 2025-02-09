FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/volcengine/verl.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /verl/. /repo && rm -rf /verl/ && \
    rm -rf /verl && \
    cd /repo && git checkout ed2eaf4e272efdbea195575319177b912e2a1a3f && \
    pip install -e /repo && \
    pip install transformers==4.47.1 && \
    pip install hydra-core==1.3.2 && \
    pip install tensordict==0.5.0 && \
    pip install numpy==2.2.1 && \
    pip install pytest==8.3.4 && \
    pip install pybind11==2.13.6 && \
    pip install codetiming==1.4.0 && \
    pip install yapf==0.43.0 && \
    pip install wandb==0.19.2 && \
    pip install ray==2.40.0 && \
    pip install pandas==2.2.3 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch" && \
    python /code_edit.py -t "/search_patch/8.patch" && \
    python /code_edit.py -t "/search_patch/9.patch" && \
    python /code_edit.py -t "/search_patch/10.patch" && \
    python /code_edit.py -t "/search_patch/11.patch" && \
    python /code_edit.py -t "/search_patch/12.patch" && \
    python /code_edit.py -t "/search_patch/13.patch" && \
    python /code_edit.py -t "/search_patch/14.patch" && \
    python /code_edit.py -t "/search_patch/15.patch"
RUN cd /repo && pytest --collect-only -q