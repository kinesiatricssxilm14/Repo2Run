FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/aidatatools/ollama-benchmark.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ollama-benchmark/. /repo && rm -rf /ollama-benchmark/ && \
    rm -rf /ollama-benchmark && \
    cd /repo && git checkout c6a5fded472370f35a158258e79f06d36313ffb1 && \
    pip install anyio==4.3.0 && \
    pip install certifi==2024.2.2 && \
    pip install charset-normalizer==3.3.2 && \
    pip install cli-exit-tools==1.2.6 && \
    pip install click==8.1.7 && \
    pip install colorama==0.4.6 && \
    pip install exceptiongroup==1.2.0 && \
    pip install fake-winreg==1.6.3 && \
    pip install GPUtil==1.4.0 && \
    pip install h11==0.14.0 && \
    pip install httpcore==1.0.5 && \
    pip install httpx==0.27.0 && \
    pip install idna==3.6 && \
    pip install lib-detect-testenv==2.0.8 && \
    pip install lib-platform==1.2.10 && \
    pip install lib-registry==2.0.10 && \
    pip install markdown-it-py==3.0.0 && \
    pip install mdurl==0.1.2 && \
    pip install ollama==0.1.8 && \
    pip install psutil==5.9.8 && \
    pip install Pygments==2.17.2 && \
    pip install PyYAML==6.0.1 && \
    pip install requests==2.31.0 && \
    pip install rich==13.7.1 && \
    pip install shellingham==1.5.4 && \
    pip install sniffio==1.3.1 && \
    pip install typer==0.9.4 && \
    pip install typing_extensions==4.10.0 && \
    pip install urllib3==2.2.1 && \
    pip install wrapt==1.16.0
ENV PYTHONPATH="/repo"
RUN cd /repo && pytest --collect-only -q