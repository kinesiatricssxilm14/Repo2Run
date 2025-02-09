FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/paulrobello/parllama.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /parllama/. /repo && rm -rf /parllama/ && \
    rm -rf /parllama && \
    cd /repo && git checkout 421238aeca193420ca112a7d1daadcebd323e9a4 && \
    pip install anthropic==0.42.0 && \
    pip install argparse==1.4.0 && \
    pip install asyncio==3.4.3 && \
    pip install attrs==24.3.0 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install build==1.2.2.post1 && \
    pip install certifi==2024.12.14 && \
    pip install charset-normalizer==3.4.1 && \
    pip install chromadb==0.5.23 && \
    pip install cryptography==44.0.0 && \
    pip install docker==7.1.0 && \
    pip install google-api-core==2.24.0 && \
    pip install google-api-python-client==2.157.0 && \
    pip install google-auth==2.37.0 && \
    pip install google-auth-httplib2==0.2.0 && \
    pip install google-generativeai==0.8.3 && \
    pip install groq==0.14.0 && \
    pip install httpx==0.27.2 && \
    pip install huggingface-hub==0.27.1 && \
    pip install humanize==4.11.0 && \
    pip install isodate2==0.9.0 && \
    pip install jsonschema==4.23.0 && \
    pip install langchain==0.3.14 && \
    pip install langchain-anthropic==0.3.1 && \
    pip install langchain-chroma==0.2.0 && \
    pip install langchain-community==0.3.14 && \
    pip install langchain-core==0.3.29 && \
    pip install langchain-experimental==0.3.4 && \
    pip install langchain-google-community==2.0.4 && \
    pip install langchain-google-genai==2.0.8 && \
    pip install langchain-groq==0.2.3 && \
    pip install langchain-huggingface==0.1.2 && \
    pip install langchain-ollama==0.2.2 && \
    pip install langchain-openai==0.2.14 && \
    pip install langchain-text-splitters==0.3.5 && \
    pip install langchainhub==0.1.21 && \
    pip install langgraph==0.2.61 && \
    pip install langsmith==0.2.10 && \
    pip install markdownify==0.14.1 && \
    pip install ollama==0.4.5 && \
    pip install openai==1.59.5 && \
    pip install pydantic==2.9.2 && \
    pip install pydantic-core==2.23.4 && \
    pip install pypdf==5.1.0 && \
    pip install pyperclip==1.9.0 && \
    pip install python-dotenv==1.0.1 && \
    pip install pytz==2024.2 && \
    pip install requests==2.32.3 && \
    pip install requests-file==2.1.0 && \
    pip install requests-oauthlib==2.0.0 && \
    pip install rich==13.9.4 && \
    pip install semver==3.0.2 && \
    pip install sentence-transformers==3.3.1 && \
    pip install sqlalchemy==2.0.36 && \
    pip install textual==1.0.0 && \
    pip install textual-fspicker==0.0.11 && \
    pip install tiktoken==0.8.0 && \
    pip install tokenizers==0.21.0 && \
    pip install urllib3==2.3.0 && \
    pip install youtube-transcript-api==0.6.3 && \
    pip install zipp==3.21.0 && \
    pip install unstructured==0.16.12 && \
    pip install watchdog==6.0.0 && \
    pip install rich-pixels==3.0.1 && \
    pip install orjson==3.10.14
ENV PYTHONPATH=/repo/src
RUN python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH=/repo/src
RUN cd /repo && pytest --collect-only -q