FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Comfy-Org/comfy-cli.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /comfy-cli/. /repo && rm -rf /comfy-cli/ && \
    rm -rf /comfy-cli && \
    cd /repo && git checkout 7711db0e0ccca10fe980c588e4d41696a63a7efa && \
    pip install charset-normalizer==3.4.0 && \
    pip install gitpython==3.1.43 && \
    pip install httpx==0.28.1 && \
    pip install mixpanel==4.10.1 && \
    pip install packaging==24.2 && \
    pip install pathspec==0.12.1 && \
    pip install psutil==6.1.0 && \
    pip install pyyaml==6.0.2 && \
    pip install questionary==2.0.1 && \
    pip install requests==2.32.3 && \
    pip install rich==13.9.4 && \
    pip install tomlkit==0.13.2 && \
    pip install typer==0.15.1 && \
    pip install typing-extensions==4.12.2 && \
    pip install uv==0.5.9 && \
    pip install websocket-client==1.8.0 && \
    pip install semver==3.0.2
ENV PYTHONPATH=/repo