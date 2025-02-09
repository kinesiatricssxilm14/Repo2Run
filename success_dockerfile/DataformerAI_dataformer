FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/DataformerAI/dataformer.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /dataformer/. /repo && rm -rf /dataformer/ && \
    rm -rf /dataformer && \
    cd /repo && git checkout 0cf88cc22a20a6d5d115773ae9aac8970d7812e3 && \
    pip install pydantic==2.10.4 && \
    pip install tiktoken==0.8.0 && \
    pip install aiohttp==3.11.11 && \
    pip install python-dotenv==1.0.1 && \
    pip install pytest==8.3.4 && \
    pip install ruff==0.4.5 && \
    pip install pre-commit==4.0.1 && \
    pip install black==24.4.2 && \
    pip install pytest-asyncio==0.25.2 && \
    pip install nest-asyncio==1.6.0 && \
    pip install pytest-timeout==2.3.1 && \
    pip install pytest-codspeed==3.1.1 && \
    pip install openai==1.59.5
ENV PYTHONPATH="$PYTHONPATH:/repo/src"
RUN pip install jinja2==3.1.5 && \
    pip install datasets==3.2.0 && \
    python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH="$PYTHONPATH:/repo/src"
RUN python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH="$PYTHONPATH:/repo/src"
RUN pip install pytest-mock==3.14.0
ENV OPENAI_API_KEY=dummy_key
ENV GROQ_API_KEY=dummy_key
ENV TOGETHER_API_KEY=dummy_key
ENV ANYSCALE_API_KEY=dummy_key
ENV DEEPINFRA_API_KEY=dummy_key
ENV OPENROUTER_API_KEY=dummy_key
ENV MONSTER_API_KEY=dummy_key
ENV ANTHROPIC_API_KEY=dummy_key
ENV MOCK_API_CALLS=True
RUN python /code_edit.py -t "/search_patch/2.patch"
RUN cd /repo && pytest --collect-only -q