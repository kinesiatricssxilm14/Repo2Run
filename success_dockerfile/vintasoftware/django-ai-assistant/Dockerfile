FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/vintasoftware/django-ai-assistant.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /django-ai-assistant/. /repo && rm -rf /django-ai-assistant/ && \
    rm -rf /django-ai-assistant && \
    cd /repo && git checkout 5b26c73d55b18a9b3df2111d4bd6597dd67db0a0 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q