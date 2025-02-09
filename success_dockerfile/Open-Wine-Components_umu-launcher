FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Open-Wine-Components/umu-launcher.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /umu-launcher/. /repo && rm -rf /umu-launcher/ && \
    rm -rf /umu-launcher && \
    cd /repo && git checkout b0c0d44e0e533b42790360d30430a69b330849d6 && \
    pip install hatch==1.14.0 hatchling==1.27.0 && \
    pip install python-xlib==0.33 && \
    pip install filelock==3.16.1 && \
    pip install black==24.10.0 && \
    pip install gitpython==3.1.43 && \
    pip install isort==5.13.2 && \
    pip install mypy==1.14.0 && \
    pip install ruff==0.8.4 && \
    pip install toml-sort==0.24.2 && \
    pip install types-pyyaml==6.0.12.20241221 && \
    pip install urllib3==2.2.3 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch"