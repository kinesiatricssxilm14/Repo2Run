FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jgravelle/pocketgroq.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /pocketgroq/. /repo && rm -rf /pocketgroq/ && \
    rm -rf /pocketgroq && \
    cd /repo && git checkout e995c4146b88e21a9e8a45aa45b11c3e30239685 && \
    pip install bs4==0.0.2 && \
    pip install groq==0.13.1 && \
    pip install python-dotenv==1.0.1 && \
    pip install pytest==8.3.4 && \
    pip install pytest-asyncio==0.25.0 && \
    pip install requests==2.32.3 && \
    pip install langchain==0.3.13 && \
    pip install langchain-groq==0.2.2 && \
    pip install langchain-community==0.3.13 && \
    pip install markdown2==2.5.2 && \
    pip install faiss-cpu==1.9.0.post1 && \
    pip install ollama==0.4.4 && \
    pip install html2text==2024.2.26 && \
    pip install streamlit==1.41.1 && \
    pip install -e /repo