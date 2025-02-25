FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/D-Star-AI/dsRAG.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /dsRAG/. /repo && rm -rf /dsRAG/ && \
    rm -rf /dsRAG && \
    cd /repo && git checkout 2d5431aa9ae2b64279dc38f429e0a0d48c53bdef && \
    pip install aiohttp==3.11.10 && \
    pip install aiolimiter==1.1.0 && \
    pip install aiosignal==1.3.1 && \
    pip install annotated-types==0.7.0 && \
    pip install anthropic==0.40.0 && \
    pip install anyio==4.7.0 && \
    pip install asgiref==3.8.1 && \
    pip install async-timeout==5.0.1 && \
    pip install attrs==23.2.0 && \
    pip install authlib==1.3.1 && \
    pip install backoff==2.2.1 && \
    pip install bcrypt==4.2.0 && \
    pip install boto3==1.34.142 && \
    pip install botocore==1.34.142 && \
    pip install build==1.2.2.post1 && \
    pip install cachetools==5.5.0 && \
    pip install certifi==2024.12.14 && \
    pip install cffi==1.16.0 && \
    pip install charset-normalizer==3.4.0 && \
    pip install chroma-hnswlib==0.7.6 && \
    pip install chromadb==0.5.5 && \
    pip install click==8.1.7 && \
    pip install cohere==5.5.8 && \
    pip install coloredlogs==15.0.1 && \
    pip install cryptography==42.0.8 && \
    pip install deprecated==1.2.14 && \
    pip install distro==1.9.0 && \
    pip install docstring-parser==0.16 && \
    pip install docx2txt==0.8 && \
    pip install durationpy==0.9 && \
    pip install exceptiongroup==1.2.2 && \
    pip install faiss-cpu==1.8.0.post1 && \
    pip install fastapi==0.115.6 && \
    pip install fastavro==1.9.5 && \
    pip install filelock==3.16.1 && \
    pip install flatbuffers==24.3.25 && \
    pip install frozenlist==1.5.0 && \
    pip install fsspec==2024.10.0 && \
    pip install google-auth==2.37.0 && \
    pip install googleapis-common-protos==1.66.0 && \
    pip install grpcio==1.68.1 && \
    pip install grpcio-health-checking==1.62.3 && \
    pip install grpcio-tools==1.62.3 && \
    pip install h11==0.14.0 && \
    pip install h2==4.1.0 && \
    pip install hpack==4.0.0 && \
    pip install httpcore==1.0.7 && \
    pip install httptools==0.6.4 && \
    pip install httpx[http2]==0.27.0 && \
    pip install httpx-sse==0.4.0 && \
    pip install huggingface-hub==0.23.4 && \
    pip install humanfriendly==10.0 && \
    pip install hyperframe==6.0.1 && \
    pip install idna==3.10 && \
    pip install importlib-metadata==8.0.0 && \
    pip install importlib-resources==6.4.5 && \
    pip install instructor==1.3.4 && \
    pip install jiter==0.4.2 && \
    pip install jmespath==1.0.1 && \
    pip install joblib==1.4.2 && \
    pip install jsonpatch==1.33 && \
    pip install jsonpointer==3.0.0 && \
    pip install jsonref==1.1.0 && \
    pip install kubernetes==31.0.0 && \
    pip install langchain-core==0.2.43 && \
    pip install langchain-text-splitters==0.2.2 && \
    pip install langsmith==0.1.147 && \
    pip install markdown-it-py==3.0.0 && \
    pip install mdurl==0.1.2 && \
    pip install mmh3==5.0.1 && \
    pip install monotonic==1.6 && \
    pip install mpmath==1.3.0 && \
    pip install multidict==6.1.0 && \
    pip install numpy==1.26.4 && \
    pip install oauthlib==3.2.2 && \
    pip install ollama==0.2.1 && \
    pip install onnxruntime==1.19.2 && \
    pip install openai==1.57.4 && \
    pip install opentelemetry-api==1.29.0 && \
    pip install opentelemetry-exporter-otlp-proto-common==1.29.0 && \
    pip install opentelemetry-exporter-otlp-proto-grpc==1.29.0 && \
    pip install opentelemetry-instrumentation==0.50b0 && \
    pip install opentelemetry-instrumentation-asgi==0.50b0 && \
    pip install opentelemetry-instrumentation-fastapi==0.50b0 && \
    pip install opentelemetry-proto==1.29.0 && \
    pip install opentelemetry-sdk==1.29.0 && \
    pip install opentelemetry-semantic-conventions==0.50b0 && \
    pip install opentelemetry-util-http==0.50b0 && \
    pip install orjson==3.10.12 && \
    pip install overrides==7.7.0 && \
    pip install packaging==24.1 && \
    pip install pandas==2.2.2 && \
    pip install parameterized==0.9.0 && \
    pip install pinecone==5.4.2 && \
    pip install portalocker==2.10.1 && \
    pip install posthog==3.7.0 && \
    pip install protobuf==5.29.1 && \
    pip install pyarrow==18.1.0 && \
    pip install pyasn1==0.6.1 && \
    pip install pyasn1-modules==0.4.1 && \
    pip install pycparser==2.22 && \
    pip install pydantic==2.10.3 && \
    pip install pydantic-core==2.27.1 && \
    pip install pygments==2.18.0 && \
    pip install pymilvus==2.5.0 && \
    pip install pypdf2==3.0.1 && \
    pip install pypika==0.48.9 && \
    pip install pyproject-hooks==1.2.0 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install python-dotenv==1.0.1 && \
    pip install pytz==2024.2 && \
    pip install pyyaml==6.0.1 && \
    pip install qdrant-client==1.12.0 && \
    pip install regex==2024.5.15 && \
    pip install requests==2.32.3 && \
    pip install requests-oauthlib==2.0.0 && \
    pip install rich==13.7.1 && \
    pip install rsa==4.9 && \
    pip install s3transfer==0.10.2 && \
    pip install scikit-learn==1.5.1 && \
    pip install scipy==1.13.1 && \
    pip install shellingham==1.5.4 && \
    pip install six==1.16.0 && \
    pip install sniffio==1.3.1 && \
    pip install starlette==0.41.3 && \
    pip install sympy==1.13.3 && \
    pip install tenacity==8.5.0 && \
    pip install threadpoolctl==3.5.0 && \
    pip install tiktoken==0.7.0 && \
    pip install tokenizers==0.19.1 && \
    pip install tqdm==4.67.1 && \
    pip install typer==0.12.3 && \
    pip install types-requests==2.31.0.6 && \
    pip install types-urllib3==1.26.25.14 && \
    pip install typing==3.7.4.3 && \
    pip install typing-extensions==4.12.2 && \
    pip install tzdata==2024.1 && \
    pip install urllib3==2.2.3 && \
    pip install uvicorn[standard]==0.34.0 && \
    pip install uvloop==0.21.0 && \
    pip install validators==0.28.3 && \
    pip install voyageai==0.2.3 && \
    pip install watchfiles==0.24.0 && \
    pip install weaviate-client==4.6.5 && \
    pip install websocket-client==1.8.0 && \
    pip install websockets==14.1 && \
    pip install wrapt==1.16.0 && \
    pip install yarl==1.18.3 && \
    pip install zipp==3.21.0 && \
    pip install vertexai==1.71.1 && \
    pip install google-generativeai==0.8.3 && \
    pip install pillow==11.0.0 && \
    pip install pdf2image==1.17.0 && \
    mv /repo/dsrag/dsparse/tests/integration/test_vlm_file_parsing.py /repo/dsrag/dsparse/tests/integration/test_vlm_file_parsing_alt.py && \
    mv /repo/dsrag/dsparse/tests/unit/test_file_system.py /repo/dsrag/dsparse/tests/unit/test_file_system_alt.py