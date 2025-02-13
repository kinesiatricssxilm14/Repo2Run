FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/JoshuaC215/agent-service-toolkit.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /agent-service-toolkit/. /repo && rm -rf /agent-service-toolkit/ && \
    rm -rf /agent-service-toolkit && \
    cd /repo && git checkout c72f48827240cb71e066f28cad03d34ad6fac300 && \
    pip install duckduckgo-search==7.2.1 fastapi==0.115.6 httpx==0.27.2 langchain-core==0.3.29 langchain-community==0.3.14 langchain-openai==0.2.14 langchain-anthropic==0.3.1 langchain-google-genai==2.0.8 langchain-groq==0.2.3 langchain-aws==0.2.10 langgraph==0.2.61 langgraph-checkpoint-sqlite==2.0.1 langsmith==0.1.147 numexpr==2.10.2 pyarrow==18.1.0 pydantic==2.10.5 pydantic-settings==2.6.1 pyowm==3.3.0 python-dotenv==1.0.1 setuptools==75.6.0 streamlit==1.40.2 tiktoken==0.8.0 uvicorn==0.32.1 pre-commit==4.0.1 pytest==8.3.4 pytest-cov==6.0.0 pytest-env==1.1.5 pytest-asyncio==0.25.2 ruff==0.9.0
RUN cd /repo && pytest --collect-only -q