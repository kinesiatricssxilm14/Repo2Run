FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/gregpr07/browser-use.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /browser-use/. /repo && rm -rf /browser-use/ && \
    rm -rf /browser-use && \
    cd /repo && git checkout 5e545d7242762b1bcc014aaabe641e72c161f6f8 && \
    cd /repo && pip install MainContentExtractor==0.0.4 beautifulsoup4==4.12.3 httpx==0.27.2 langchain==0.3.12 langchain-openai==0.2.12 langchain-anthropic==0.3.0 langchain-fireworks==0.2.5 pydantic==2.10.3 python-dotenv==1.0.1 requests==2.32.3 posthog==3.7.4 playwright==1.49.1 && \
    cd /repo && pip install pytest==8.3.4 pytest-asyncio==0.25.0
ENV OPENAI_API_KEY=example_key