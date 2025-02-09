FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/iterative/datachain.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /datachain/. /repo && rm -rf /datachain/ && \
    rm -rf /datachain && \
    cd /repo && git checkout b67d599df627b47feec2bc7a30938e0f1a602edb && \
    pip install pyyaml==6.0.2 && \
    pip install tomlkit==0.13.2 && \
    pip install tqdm==4.67.1 && \
    pip install numpy==2.2.1 && \
    pip install pandas==2.2.3 && \
    pip install pyarrow==18.1.0 && \
    pip install typing-extensions==4.12.2 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install attrs==24.3.0 && \
    pip install s3fs==2024.12.0 && \
    pip install gcsfs==2024.12.0 && \
    pip install adlfs==2024.12.0 && \
    pip install dvc-data==3.16.7 && \
    pip install dvc-objects==5.1.0 && \
    pip install shtab==1.7.1 && \
    pip install sqlalchemy==2.0.37 && \
    pip install multiprocess==0.70.16 && \
    pip install cloudpickle==3.1.0 && \
    pip install orjson==3.10.14 && \
    pip install pydantic==2.10.5 && \
    pip install jmespath==1.0.1 && \
    pip install datamodel-code-generator==0.26.4 && \
    pip install pillow==11.1.0 && \
    pip install msgpack==1.1.0 && \
    pip install psutil==6.1.1 && \
    pip install huggingface_hub==0.27.1 && \
    pip install iterative-telemetry==0.0.9 && \
    pip install platformdirs==4.3.6 && \
    pip install dvc-studio-client==0.21.0 && \
    pip install tabulate==0.9.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-sugar==1.0.0 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-mock==3.14.0 && \
    pip install pytest-servers==0.5.9 && \
    pip install pytest-benchmark==5.1.0 && \
    pip install pytest-xdist==3.6.1 && \
    pip install virtualenv==20.28.1 && \
    pip install dulwich==0.22.7 && \
    pip install hypothesis==6.123.13 && \
    pip install open_clip_torch==2.30.0 && \
    pip install aiotools==1.7.0 && \
    pip install requests-mock==1.12.1 && \
    pip install scipy==1.15.0 && \
    pip install mypy==1.14.1 && \
    pip install types-python-dateutil==2.9.0.20241206 && \
    pip install types-pytz==2024.2.0.20241221 && \
    pip install types-pyyaml==6.0.12.20241230 && \
    pip install types-requests==2.32.0.20241016 && \
    pip install types-tabulate==0.9.0.20241207
ENV PYTHONPATH=/repo/src
RUN pip install lz4==4.3.3 && \
    pip install datasets==3.2.0 && \
    pip install transformers==4.47.1
ENV PYTHONPATH=/repo/src
RUN cd /repo && pytest --collect-only -q