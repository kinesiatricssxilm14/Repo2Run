FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/andrewyng/translation-agent.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /translation-agent/. /repo && rm -rf /translation-agent/ && \
    rm -rf /translation-agent && \
    cd /repo && git checkout e0fc605acbb5d78cb7a58a98bc8bd8f0056df49c && \
    cd /repo && poetry install && \
    cd /repo && poetry run pip list && \
    pip install openai==1.57.4 && \
    pip install python-dotenv==1.0.1
ENV PYTHONPATH=/repo/src:$PYTHONPATH
RUN pip install tiktoken==0.8.0 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    pip install icecream==2.1.3 && \
    pip install langchain-text-splitters==0.3.3
ENV OPENAI_API_KEY="dummy_key"