FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/bananaml/fructose.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fructose/. /repo && rm -rf /fructose/ && \
    rm -rf /fructose && \
    cd /repo && git checkout 5f24ec0f773170d5f55fe520fa7436f69b1a4f65 && \
    cd /repo && pip install -e .
ENV OPENAI_API_KEY="your_openai_api_key"