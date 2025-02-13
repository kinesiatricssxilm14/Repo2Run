FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/leopiney/neuralnoise.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /neuralnoise/. /repo && rm -rf /neuralnoise/ && \
    rm -rf /neuralnoise && \
    cd /repo && git checkout c0313feb10b4474ed4418d2aeef24b48649c641b && \
    pip install autogen-agentchat==0.2.40 && \
    pip install backoff==2.2.1 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install crawl4ai==0.4.23 && \
    pip install elevenlabs==1.50.3 && \
    pip install langchain-community==0.3.13 && \
    pip install lxml==5.3.0 && \
    pip install openai==1.58.1 && \
    pip install pydantic==2.10.4 && \
    pip install pydub==0.25.1 && \
    pip install pymupdf==1.25.1 && \
    pip install python-dotenv==1.0.1 && \
    pip install tabulate==0.9.0 && \
    pip install tqdm==4.67.1 && \
    pip install typer==0.15.1 && \
    pip install youtube-transcript-api==0.6.3