FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/apple/ToolSandbox.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ToolSandbox/. /repo && rm -rf /ToolSandbox/ && \
    rm -rf /ToolSandbox && \
    cd /repo && git checkout 1a1dc83bd84948f0a3d3ace0e59923fc760c111b && \
    pip install anthropic==0.26.1 && \
    pip install ccy==1.3.1 && \
    pip install decorator==5.1.1 && \
    pip install dill==0.3.8 && \
    pip install geopy==2.4.1 && \
    pip install holidays==0.51 && \
    pip install huggingface_hub==0.23.4 && \
    pip install jsonschema==4.19.2 && \
    pip install langchain==0.1.3 && \
    pip install networkx==3.2.1 && \
    pip install numpy==1.26.4 && \
    pip install openai==1.17.0 && \
    pip install phonenumbers==8.13.39 && \
    pip install pint==0.23 && \
    pip install polars==0.20.31 && \
    pip install pydantic==2.7.4 && \
    pip install pyyaml==6.0.1 && \
    pip install rapidfuzz==3.9.3 && \
    pip install requests==2.32.3 && \
    pip install rouge-score==0.1.2 && \
    pip install scipy==1.13.1 && \
    pip install sentencepiece==0.2.0 && \
    pip install strenum==0.4.15 && \
    pip install tenacity==8.4.1 && \
    pip install transformers==4.41.2 && \
    pip install tree-sitter==0.22.3 && \
    pip install tree-sitter-languages==1.10.2 && \
    pip install typing_extensions==4.12.2 && \
    pip install vertexai==1.49.0