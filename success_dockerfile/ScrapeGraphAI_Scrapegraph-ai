FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ScrapeGraphAI/Scrapegraph-ai.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Scrapegraph-ai/. /repo && rm -rf /Scrapegraph-ai/ && \
    rm -rf /Scrapegraph-ai && \
    cd /repo && git checkout bae92b0dcca353c137f8cdb12ef95b3bc2cd962a && \
    pip install langchain==0.3.14 && \
    pip install langchain-google-genai==2.0.8 && \
    pip install langchain-openai==0.2.14 && \
    pip install langchain-mistralai==0.2.4 && \
    pip install langchain_community==0.3.14 && \
    pip install langchain-aws==0.2.10 && \
    pip install html2text==2024.2.26 && \
    pip install faiss-cpu==1.9.0.post1 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install pandas==2.2.3 && \
    pip install python-dotenv==1.0.1 && \
    pip install tiktoken==0.7.0 && \
    pip install tqdm==4.67.1 && \
    pip install minify-html==0.15.0 && \
    pip install free-proxy==1.1.3 && \
    pip install playwright==1.49.1 && \
    pip install undetected-playwright==0.3.0 && \
    pip install semchunk==3.0.0 && \
    pip install langchain-ollama==0.2.2 && \
    pip install simpleeval==1.0.3 && \
    pip install googlesearch-python==1.2.5 && \
    pip install async_timeout==4.0.3 && \
    pip install pytest==8.0.0 && \
    pip install pytest-mock==3.14.0 && \
    pip install burr[start]==0.22.1 && \
    pip install sphinx==6.0.0 && \
    pip install furo==2024.5.6 && \
    pip install pylint==3.3.3
ENV PYTHONPATH=$PYTHONPATH:/repo
RUN pip install qdrant-client==1.12.2 && \
    cd /repo && pip install -e . && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch"
RUN cd /repo && pytest --collect-only -q