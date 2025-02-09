FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/daxa-ai/pebblo.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /pebblo/. /repo && rm -rf /pebblo/ && \
    rm -rf /pebblo && \
    cd /repo && git checkout e67b01121b7140ae6448941fb10c2f257515d1b0 && \
    pip install torch==2.5.1 && \
    pip install jinja2==3.1.2 && \
    pip install tqdm==4.64.1 && \
    pip install transformers==4.24.0 && \
    pip install xhtml2pdf==0.2.16 && \
    pip install fastapi==0.115.6 && \
    pip install tqdm==4.64.1 && \
    pip install uvicorn==0.34.0 && \
    pip install pydantic==2.10.3 && \
    pip install google_api_python_client==2.155.0 && \
    pip install huggingface_hub==0.10.0 && \
    pip install Jinja2==3.1.2 && \
    pip install langchain_community==0.3.12 && \
    pip install langchain_google_community==2.0.3 && \
    pip install langchain_openai==0.2.12 && \
    pip install langchain_pinecone==0.2.0 && \
    pip install langchain_postgres==0.0.12 && \
    pip install llama_index==0.12.5 && \
    pip install pinecone==5.4.2 && \
    pip install presidio_analyzer==2.2.356 && \
    pip install presidio_anonymizer==2.2.356 && \
    pip install protobuf==5.29.1 && \
    pip install pydantic_settings==2.7.0 && \
    pip install pytest==7.1.2 && \
    pip install python-dotenv==1.0.1 && \
    pip install python_dateutil==2.8.2 && \
    pip install PyYAML==6.0.2 && \
    pip install Requests==2.32.3 && \
    pip install shortuuid==1.0.13 && \
    pip install SQLAlchemy==1.4.39 && \
    pip install starlette==0.42.0 && \
    pip install toml==0.10.2 && \
    pip install weasyprint==63.1 && \
    pip install huggingface_hub==0.10.0 && \
    pip install fastapi==0.115.6 && \
    pip install google_api_python_client==2.155.0 && \
    pip install Jinja2==3.1.2 && \
    pip install langchain_community==0.3.12 && \
    pip install langchain_google_community==2.0.3 && \
    pip install langchain_openai==0.2.12 && \
    pip install langchain_pinecone==0.2.0 && \
    pip install langchain_postgres==0.0.12 && \
    pip install llama_index==0.12.5 && \
    pip install pinecone==5.4.2 && \
    pip install presidio_analyzer==2.2.356 && \
    pip install presidio_anonymizer==2.2.356 && \
    pip install protobuf==5.29.1 && \
    pip install pydantic==2.10.3 && \
    pip install pydantic_settings==2.7.0 && \
    pip install pytest==7.1.2 && \
    pip install python-dotenv==1.0.1 && \
    pip install python_dateutil==2.8.2 && \
    pip install PyYAML==6.0.2 && \
    pip install Requests==2.32.3 && \
    pip install shortuuid==1.0.13 && \
    pip install SQLAlchemy==1.4.39 && \
    pip install starlette==0.42.0 && \
    pip install toml==0.10.2 && \
    pip install tqdm==4.64.1 && \
    pip install transformers==4.24.0 && \
    pip install uvicorn==0.34.0 && \
    pip install weasyprint==63.1 && \
    pip install xhtml2pdf==0.2.16 && \
    pip install tqdm==4.64.1 && \
    pip install jinja2==3.1.2 && \
    pip install pydantic==2.10.3 && \
    pip install huggingface_hub==0.9.0 && \
    pip install huggingface_hub==0.10.0 && \
    python /code_edit.py -t "/search_patch/0.patch"