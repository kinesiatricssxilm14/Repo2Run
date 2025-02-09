FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/crewAIInc/crewAI-tools.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /crewAI-tools/. /repo && rm -rf /crewAI-tools/ && \
    rm -rf /crewAI-tools && \
    cd /repo && git checkout 8739359d3153823df656228dc287914ceae513fc && \
    pip install pydantic==2.10.4 && \
    pip install pytest==8.3.4 && \
    pip install lancedb==0.17.0 && \
    pip install openai==1.59.5 && \
    pip install chromadb==0.5.23 && \
    pip install pyright==1.1.391 && \
    pip install pytube==15.0.0 && \
    pip install requests==2.32.3 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install selenium==4.27.1 && \
    pip install docx2txt==0.8 && \
    pip install docker==7.1.0 && \
    pip install embedchain==0.1.126 && \
    pip install crewai==0.95.0
ENV PYTHONPATH=$PYTHONPATH:/repo/crewai_tools
RUN pip install weaviate-client==4.10.2 && \
    python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=$PYTHONPATH:/repo/crewai_tools
ENV OPENAI_API_KEY="your_openai_api_key"
ENV PYTHONPATH=$PYTHONPATH:/repo/crewai_tools
RUN python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH=/repo/crewai_tools
RUN python -c "import sys; print(sys.path)" && \
    pip install -e /repo
ENV OPENAI_API_KEY="your_openai_api_key"
RUN python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch"
ENV PYTHONPATH=/repo/crewai_tools
ENV OPENAI_API_KEY="your_openai_api_key"
RUN cd /repo && pytest --collect-only -q