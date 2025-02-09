FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ZenGuard-AI/fast-llm-security-guardrails.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fast-llm-security-guardrails/. /repo && rm -rf /fast-llm-security-guardrails/ && \
    rm -rf /fast-llm-security-guardrails && \
    cd /repo && git checkout 6a867c1eebd8eb5579728385e9ae317af480a256 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q