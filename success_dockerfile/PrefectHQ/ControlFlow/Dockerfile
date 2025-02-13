FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/PrefectHQ/ControlFlow.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ControlFlow/. /repo && rm -rf /ControlFlow/ && \
    rm -rf /ControlFlow && \
    cd /repo && git checkout f259fa8144ed31b8bde5902a2de8548dd4601ce5 && \
    pip install aiosqlite==0.20.0 && \
    pip install alembic==1.13.2 && \
    pip install annotated-types==0.7.0 && \
    pip install anthropic==0.42.0 && \
    pip install anyio==4.4.0 && \
    pip install apprise==1.9.0 && \
    pip install asgi-lifespan==2.1.0 && \
    pip install asyncpg==0.29.0 && \
    pip install attrs==24.2.0 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install cachetools==5.5.0 && \
    pip install certifi==2024.8.30 && \
    pip install cffi==1.17.0 && \
    pip install charset-normalizer==3.4.1 && \
    pip install click==8.1.7 && \
    pip install cloudpickle==3.0.0 && \
    pip install colorama==0.4.6 && \
    pip install coolname==2.2.0 && \
    pip install croniter==3.0.3 && \
    pip install cryptography==43.0.1 && \
    pip install dateparser==1.2.0 && \
    pip install defusedxml==0.7.1 && \
    pip install distro==1.9.0 && \
    pip install docker==7.1.0 && \
    pip install exceptiongroup==1.2.2 && \
    pip install fastapi==0.115.6 && \
    pip install filelock==3.15.4 && \
    pip install fsspec==2024.6.1 && \
    pip install graphviz==0.20.3 && \
    pip install greenlet==3.0.3 && \
    pip install griffe==1.5.4 && \
    pip install h11==0.14.0 && \
    pip install h2==4.1.0 && \
    pip install hpack==4.0.0 && \
    pip install httpcore==1.0.5 && \
    pip install httpx==0.27.2 && \
    pip install huggingface-hub==0.24.6 && \
    pip install humanize==4.10.0 && \
    pip install hyperframe==6.0.1 && \
    pip install idna==3.8 && \
    pip install jinja2==3.1.5 && \
    pip install jinja2-humanize-extension==0.4.0 && \
    pip install jiter==0.5.0 && \
    pip install jsonpatch==1.33 && \
    pip install jsonpointer==3.0.0 && \
    pip install jsonschema==4.23.0 && \
    pip install jsonschema-specifications==2023.12.1 && \
    pip install langchain-anthropic==0.3.1 && \
    pip install langchain-core==0.3.29 && \
    pip install langchain-openai==0.2.14 && \
    pip install langsmith==0.2.10 && \
    pip install linkify-it-py==2.0.3 && \
    pip install mako==1.3.5 && \
    pip install markdown==3.7 && \
    pip install markdown-it-py==3.0.0 && \
    pip install markdownify==0.13.1 && \
    pip install markupsafe==2.1.5 && \
    pip install mdit-py-plugins==0.4.1 && \
    pip install mdurl==0.1.2 && \
    pip install oauthlib==3.2.2 && \
    pip install openai==1.59.4 && \
    pip install orjson==3.10.7 && \
    pip install packaging==24.1 && \
    pip install pathspec==0.12.1 && \
    pip install pendulum==3.0.0 && \
    pip install platformdirs==4.2.2 && \
    pip install prefect==3.0.0 && \
    pip install prometheus-client==0.20.0 && \
    pip install pycparser==2.22 && \
    pip install pydantic==2.10.4 && \
    pip install pydantic-core==2.27.2 && \
    pip install pydantic-extra-types==2.10.1 && \
    pip install pydantic-settings==2.7.1 && \
    pip install pygments==2.18.0 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install python-dotenv==1.0.1 && \
    pip install python-slugify==8.0.4 && \
    pip install pytz==2024.1 && \
    pip install pyyaml==6.0.2 && \
    pip install readchar==4.2.0 && \
    pip install referencing==0.35.1 && \
    pip install regex==2024.7.24 && \
    pip install requests==2.32.3 && \
    pip install requests-oauthlib==2.0.0 && \
    pip install rfc3339-validator==0.1.4 && \
    pip install rich==13.8.0 && \
    pip install rpds-py==0.20.0 && \
    pip install ruamel-yaml==0.18.6 && \
    pip install ruamel-yaml-clib==0.2.8 && \
    pip install shellingham==1.5.4 && \
    pip install six==1.16.0 && \
    pip install sniffio==1.3.1 && \
    pip install soupsieve==2.6 && \
    pip install sqlalchemy==2.0.33 && \
    pip install starlette==0.41.3 && \
    pip install tenacity==8.5.0 && \
    pip install text-unidecode==1.3 && \
    pip install textual==1.0.0 && \
    pip install tiktoken==0.7.0 && \
    pip install time-machine==2.15.0 && \
    pip install tokenizers==0.20.0 && \
    pip install toml==0.10.2 && \
    pip install tqdm==4.66.5 && \
    pip install typer==0.15.1 && \
    pip install typing-extensions==4.12.2 && \
    pip install tzdata==2024.1 && \
    pip install tzlocal==5.2 && \
    pip install uc-micro-py==1.0.3 && \
    pip install ujson==5.10.0 && \
    pip install urllib3==2.2.2 && \
    pip install uvicorn==0.34.0 && \
    pip install websockets==13.0.1
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install chromadb==0.6.2
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install langchain_community==0.3.14 && \
    pip install langchain_google_genai==2.0.8
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install pydantic==1.10.12
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip uninstall -y pydantic-extra-types
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install pydantic-extra-types==0.0.1
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install pydantic==2.8.2 && \
    pip install pydantic-extra-types==2.9.0
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install pipreqs==0.5.0 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    pipreqs /repo --force && \
    pip install chromadb==0.6.2 && \
    pip install fastapi==0.115.6 && \
    pip install httpx==0.27.2 && \
    pip install Jinja2==3.1.5 && \
    pip install langchain_anthropic==0.3.1 && \
    pip install langchain_community==0.3.14 && \
    pip install langchain_core==0.3.29 && \
    pip install langchain_google_community==2.0.4 && \
    pip install langchain_google_genai==2.0.8 && \
    pip install langchain_google_vertexai==2.0.10 && \
    pip install langchain_groq==0.2.3 && \
    pip install langchain_openai==0.2.14 && \
    pip install markdownify==0.13.1 && \
    pip install pydantic==2.10.4 && \
    pip install pydantic_core==2.27.2 && \
    pip install pydantic_extra_types==2.10.1 && \
    pip install pydantic_settings==2.7.1 && \
    pip install pytest==8.3.4 && \
    pip install raggy==0.2.6 && \
    pip install textual==1.0.0 && \
    pip install tiktoken==0.7.0 && \
    pip install typer==0.15.1 && \
    pip install typing_extensions==4.12.2 && \
    pip install uvicorn==0.34.0
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN cd /repo && pytest --collect-only -q