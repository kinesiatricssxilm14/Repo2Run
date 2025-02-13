FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Codium-ai/AlphaCodium.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /AlphaCodium/. /repo && rm -rf /AlphaCodium/ && \
    rm -rf /AlphaCodium && \
    cd /repo && git checkout eb7577dbe998ae7e55696264591ac3c5dde75638 && \
    pip install dynaconf==3.1.12 && \
    pip install fastapi==0.99.0 && \
    pip install retry==0.9.2 && \
    pip install Jinja2==3.1.2 && \
    pip install tiktoken==0.8.0 && \
    pip install uvicorn==0.22.0 && \
    pip install pytest==7.4.0 && \
    pip install aiohttp==3.9.3 && \
    pip install atlassian-python-api==3.39.0 && \
    pip install GitPython==3.1.32 && \
    pip install PyYAML==6.0.1 && \
    pip install starlette-context==0.3.6 && \
    pip install boto3==1.28.25 && \
    pip install google-cloud-storage==2.10.0 && \
    pip install ujson==5.8.0 && \
    pip install azure-devops==7.1.0b3 && \
    pip install msrest==0.7.1 && \
    pip install openai==1.58.1 && \
    pip install litellm==1.55.7 && \
    pip install duckdb==0.9.2 && \
    pip install datasets==3.2.0 && \
    pip install notebook==7.3.1 && \
    pip install black==24.10.0 && \
    pip install evaluate==0.4.3 && \
    pip install click==8.1.7 && \
    pip install code_contests_tester==0.1.6 && \
    pip install aiolimiter==1.2.1 && \
    pip install tqdm==4.67.1 && \
    pip install pysnooper==1.2.1 && \
    pip install loguru==0.7.3 && \
    pip install numpy==2.2.0 && \
    pip install pydantic==2.10.4
ENV PYTHONPATH=/repo