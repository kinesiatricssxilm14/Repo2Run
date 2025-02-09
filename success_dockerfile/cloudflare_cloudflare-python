FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/cloudflare/cloudflare-python.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /cloudflare-python/. /repo && rm -rf /cloudflare-python/ && \
    rm -rf /cloudflare-python && \
    cd /repo && git checkout 22847982359f4a7d0170e69e686049e53714131e && \
    pip install annotated-types==0.6.0 && \
    pip install anyio==4.4.0 && \
    pip install certifi==2023.7.22 && \
    pip install distro==1.8.0 && \
    pip install exceptiongroup==1.1.3 && \
    pip install h11==0.14.0 && \
    pip install httpcore==1.0.2 && \
    pip install httpx==0.25.2 && \
    pip install idna==3.4 && \
    pip install pydantic==2.7.1 && \
    pip install pydantic-core==2.18.2 && \
    pip install sniffio==1.3.0 && \
    pip install typing-extensions==4.8.0 && \
    pip install argcomplete==3.1.2 && \
    pip install attrs==23.1.0 && \
    pip install colorlog==6.7.0 && \
    pip install dirty-equals==0.6.0 && \
    pip install distlib==0.3.7 && \
    pip install filelock==3.12.4 && \
    pip install importlib-metadata==7.0.0 && \
    pip install iniconfig==2.0.0 && \
    pip install markdown-it-py==3.0.0 && \
    pip install mdurl==0.1.2 && \
    pip install mypy==1.10.1 && \
    pip install mypy-extensions==1.0.0 && \
    pip install nodeenv==1.8.0 && \
    pip install nox==2023.4.22 && \
    pip install packaging==23.2 && \
    pip install platformdirs==3.11.0 && \
    pip install pluggy==1.3.0 && \
    pip install py==1.11.0 && \
    pip install pygments==2.18.0 && \
    pip install pyright==1.1.364 && \
    pip install pytest==7.1.1 && \
    pip install pytest-asyncio==0.21.1 && \
    pip install python-dateutil==2.8.2 && \
    pip install pytz==2023.3.post1 && \
    pip install respx==0.20.2 && \
    pip install rich==13.7.1 && \
    pip install ruff==0.1.9 && \
    pip install setuptools==68.2.2 && \
    pip install six==1.16.0 && \
    pip install time-machine==2.9.0 && \
    pip install tomli==2.0.1 && \
    pip install virtualenv==20.24.5 && \
    pip install zipp==3.17.0 && \
    pip install -e /repo
RUN cd /repo && pytest --collect-only -q