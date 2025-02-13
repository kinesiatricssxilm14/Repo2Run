FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/reka-ai/reka-vibe-eval.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /reka-vibe-eval/. /repo && rm -rf /reka-vibe-eval/ && \
    rm -rf /reka-vibe-eval && \
    cd /repo && git checkout 93ecd92fec87ebda5263affba744df40cc233609 && \
    pip install reka-api==1.0.6 && \
    pip install requests==2.32.3 && \
    pip install tqdm==4.67.1
ENV PYTHONPATH=/repo