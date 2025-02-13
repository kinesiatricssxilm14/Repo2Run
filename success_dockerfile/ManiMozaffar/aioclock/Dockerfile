FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ManiMozaffar/aioclock.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /aioclock/. /repo && rm -rf /aioclock/ && \
    rm -rf /aioclock && \
    cd /repo && git checkout 3d196b2642f84acdbbdca6d383f62067b33e4a9d && \
    pip install annotated-types==0.7.0 && \
    pip install anyio==4.3.0 && \
    pip install asyncer==0.0.7 && \
    pip install babel==2.15.0 && \
    pip install black==24.4.2 && \
    pip install cachetools==5.3.3 && \
    pip install certifi==2024.2.2 && \
    pip install chardet==5.2.0 && \
    pip install charset-normalizer==3.3.2 && \
    pip install click==8.1.7 && \
    pip install colorama==0.4.6 && \
    pip install croniter==2.0.5 && \
    pip install distlib==0.3.8 && \
    pip install dnspython==2.6.1 && \
    pip install email-validator==2.1.1 && \
    pip install fast-depends==2.4.3 && \
    pip install fastapi==0.111.0 && \
    pip install fastapi-cli==0.0.4 && \
    pip install filelock==3.14.0 && \
    pip install ghp-import==2.1.0 && \
    pip install griffe==0.45.2 && \
    pip install h11==0.14.0 && \
    pip install httpcore==1.0.5 && \
    pip install httptools==0.6.1 && \
    pip install httpx==0.27.0 && \
    pip install idna==3.7 && \
    pip install importlib-metadata==7.1.0 && \
    pip install importlib-resources==6.4.0 && \
    pip install iniconfig==2.0.0 && \
    pip install jinja2==3.1.4 && \
    pip install markdown==3.6 && \
    pip install markdown-it-py==3.0.0 && \
    pip install markupsafe==2.1.5 && \
    pip install mdurl==0.1.2 && \
    pip install mergedeep==1.3.4 && \
    pip install mike==2.0.0 && \
    pip install mkdocs==1.6.0 && \
    pip install mkdocs-autorefs==1.0.1 && \
    pip install mkdocs-get-deps==0.2.0 && \
    pip install mkdocs-material==9.5.24 && \
    pip install mkdocs-material-extensions==1.3.1 && \
    pip install mkdocs-simple-hooks==0.1.5 && \
    pip install mkdocstrings==0.25.1 && \
    pip install mkdocstrings-python==1.10.3 && \
    pip install mypy-extensions==1.0.0 && \
    pip install nodeenv==1.8.0 && \
    pip install orjson==3.10.3 && \
    pip install packaging==24.0 && \
    pip install paginate==0.5.6 && \
    pip install pathspec==0.12.1 && \
    pip install platformdirs==4.2.2 && \
    pip install pluggy==1.5.0 && \
    pip install pydantic==2.9.0 && \
    pip install pydantic-core==2.23.2 && \
    pip install pygments==2.18.0 && \
    pip install pymdown-extensions==10.8.1 && \
    pip install pyparsing==3.1.2 && \
    pip install pyproject-api==1.6.1 && \
    pip install pyright==1.1.364 && \
    pip install pytest==8.2.1 && \
    pip install pytest-asyncio==0.23.7 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install python-dotenv==1.0.1 && \
    pip install python-multipart==0.0.9 && \
    pip install pytz==2024.1 && \
    pip install pyyaml==6.0.1 && \
    pip install pyyaml-env-tag==0.1 && \
    pip install regex==2024.5.15 && \
    pip install requests==2.32.2 && \
    pip install rich==13.7.1 && \
    pip install ruff==0.4.5 && \
    pip install setuptools==70.0.0 && \
    pip install shellingham==1.5.4 && \
    pip install six==1.16.0 && \
    pip install sniffio==1.3.1 && \
    pip install starlette==0.37.2 && \
    pip install tox==4.15.0 && \
    pip install typer==0.12.3 && \
    pip install typing-extensions==4.12.0 && \
    pip install tzdata==2024.1 && \
    pip install ujson==5.10.0 && \
    pip install urllib3==2.2.1 && \
    pip install uvicorn==0.29.0 && \
    pip install uvloop==0.19.0 && \
    pip install verspec==0.1.0 && \
    pip install virtualenv==20.26.2 && \
    pip install watchdog==4.0.1 && \
    pip install watchfiles==0.21.0 && \
    pip install websockets==12.0 && \
    pip install zipp==3.18.2