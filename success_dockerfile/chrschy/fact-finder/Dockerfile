FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/chrschy/fact-finder.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fact-finder/. /repo && rm -rf /fact-finder/ && \
    rm -rf /fact-finder && \
    cd /repo && git checkout ca57d1b9e3683d026ae52c3662b016781d26cc97 && \
    echo "chainlit" >> /tmp/requirements.txt && \
    echo "langchain" >> /tmp/requirements.txt && \
    echo "langchain-openai" >> /tmp/requirements.txt && \
    echo "pandas" >> /tmp/requirements.txt && \
    echo "pyvis" >> /tmp/requirements.txt && \
    echo "streamlit" >> /tmp/requirements.txt && \
    echo "nltk" >> /tmp/requirements.txt && \
    echo "SPARQLWrapper" >> /tmp/requirements.txt && \
    echo "neo4j" >> /tmp/requirements.txt && \
    echo "regex" >> /tmp/requirements.txt && \
    pip install -r /tmp/requirements.txt && \
    pip install pytest==8.3.4 sentence-transformers==3.3.1
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install langchain_community==0.3.12
RUN cd /repo && pytest --collect-only -q