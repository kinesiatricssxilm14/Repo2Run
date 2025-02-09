FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/wy-z/container-vm.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /container-vm/. /repo && rm -rf /container-vm/ && \
    rm -rf /container-vm && \
    cd /repo && git checkout 07d40217758b4ab800237b2c8b8ac737aba51234 && \
    pip install typer==0.15.1 && \
    pip install pydantic==2.10.3 && \
    pip install dynaconf==3.2.6 && \
    pip install setuptools_scm==8.1.0 && \
    pip install pip-tools==7.4.1 && \
    pip install ruff==0.8.3 && \
    pip install isort==5.13.2 && \
    pip install mypy==1.13.0 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install pyinstaller==6.11.1 && \
    pip install pyinstaller-hooks-contrib==2024.10 && \
    apt-get update -qq && \
    apt-get update -qq && \
    apt-get install qemu-system -y -qq