FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ServiceNow/TapeAgents.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /TapeAgents/. /repo && rm -rf /TapeAgents/ && \
    rm -rf /TapeAgents && \
    cd /repo && git checkout 3eca5cc8841d64c5db80cadf0d8570bbdc579de2 && \
    cd /repo && pip install -e . && \
    pip install accelerate==1.2.1 && \
    pip install testbook==0.4.2 && \
    pip install wandb==0.19.1 && \
    pip install peft==0.14.0 && \
    pip install pdf2image==1.17.0 && \
    pip install ffmpeg==1.4 && \
    pip install webvtt-py==0.5.1 && \
    pip install whisper==1.1.10 && \
    pip install yt-dlp==2024.12.13 && \
    pip install openai-whisper==20240930 && \
    pip install markdownify==0.14.1 && \
    pip install python-pptx==1.0.2 && \
    pip install puremagic==1.28 && \
    pip install readability==0.3.1 && \
    pip install readability-lxml==0.8.1 && \
    pip install lxml_html_clean==0.4.1 && \
    pip install dspy==2.5.43
RUN cd /repo && pytest --collect-only -q