FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/frdel/agent-zero.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /agent-zero/. /repo && rm -rf /agent-zero/ && \
    rm -rf /agent-zero && \
    cd /repo && git checkout 3cefa150c36f6872bd9e78bb1e35aaeff38bc7be && \
    pip install ansio==0.0.1 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install docker==7.1.0 && \
    pip install duckduckgo-search==6.1.12 && \
    pip install faiss-cpu==1.8.0.post1 && \
    pip install flask[async]==3.0.3 && \
    pip install flask-basicauth==0.2.0 && \
    pip install inputimeout==1.0.4 && \
    pip install langchain-anthropic==0.1.19 && \
    pip install langchain-community==0.2.7 && \
    pip install langchain-google-genai==1.0.7 && \
    pip install langchain-groq==0.1.6 && \
    pip install langchain-huggingface==0.0.3 && \
    pip install langchain-mistralai==0.1.8 && \
    pip install langchain-ollama==0.1.3 && \
    pip install langchain-openai==0.1.15 && \
    pip install lxml_html_clean==0.3.1 && \
    pip install markdown==3.7 && \
    pip install newspaper3k==0.2.8 && \
    pip install paramiko==3.4.0 && \
    pip install pypdf==4.3.1 && \
    pip install python-dotenv==1.0.1 && \
    pip install sentence-transformers==3.0.1 && \
    pip install unstructured==0.15.13 && \
    pip install unstructured-client==0.25.9 && \
    pip install webcolors==24.6.0