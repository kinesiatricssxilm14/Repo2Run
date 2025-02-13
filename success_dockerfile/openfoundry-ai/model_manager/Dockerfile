FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/openfoundry-ai/model_manager.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /model_manager/. /repo && rm -rf /model_manager/ && \
    rm -rf /model_manager && \
    cd /repo && git checkout 34f9ffc3e1962aa87ca088203535d8d0506b4e7b && \
    pip install aiohttp==3.9.5 && \
    pip install aiosignal==1.3.1 && \
    pip install annotated-types==0.6.0 && \
    pip install anyio==4.3.0 && \
    pip install attrs==23.2.0 && \
    pip install blessed==1.20.0 && \
    pip install boto3==1.34.65 && \
    pip install botocore==1.34.65 && \
    pip install certifi==2024.2.2 && \
    pip install charset-normalizer==3.3.2 && \
    pip install click==8.1.7 && \
    pip install cloudpickle==2.2.1 && \
    pip install contextlib2==21.6.0 && \
    pip install datasets==2.19.0 && \
    pip install dill==0.3.8 && \
    pip install docker==7.0.0 && \
    pip install editor==1.6.6 && \
    pip install fastapi==0.110.1 && \
    pip install filelock==3.13.1 && \
    pip install frozenlist==1.4.1 && \
    pip install fsspec==2024.3.1 && \
    pip install google-pasta==0.2.0 && \
    pip install h11==0.14.0 && \
    pip install httptools==0.6.1 && \
    pip install huggingface-hub==0.21.4 && \
    pip install idna==3.7 && \
    pip install importlib-metadata==6.11.0 && \
    pip install inquirer==3.2.4 && \
    pip install inquirerpy==0.3.4 && \
    pip install jmespath==1.0.1 && \
    pip install jsonschema==4.21.1 && \
    pip install jsonschema-specifications==2023.12.1 && \
    pip install markdown-it-py==3.0.0 && \
    pip install mdurl==0.1.2 && \
    pip install multidict==6.0.5 && \
    pip install multiprocess==0.70.16 && \
    pip install numpy==1.26.4 && \
    pip install packaging==24.0 && \
    pip install pandas==2.2.1 && \
    pip install pathos==0.3.2 && \
    pip install pfzy==0.3.4 && \
    pip install platformdirs==4.2.0 && \
    pip install pox==0.3.4 && \
    pip install ppft==1.7.6.8 && \
    pip install prompt-toolkit==3.0.43 && \
    pip install protobuf==4.25.3 && \
    pip install psutil==5.9.8 && \
    pip install pyarrow==16.0.0 && \
    pip install pyarrow-hotfix==0.6 && \
    pip install pydantic==2.6.4 && \
    pip install pydantic-core==2.16.3 && \
    pip install pygments==2.17.2 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install python-dotenv==1.0.1 && \
    pip install pytz==2024.1 && \
    pip install pyyaml==6.0.1 && \
    pip install readchar==4.0.6 && \
    pip install referencing==0.34.0 && \
    pip install regex==2024.4.28 && \
    pip install requests==2.31.0 && \
    pip install rich==13.7.1 && \
    pip install rpds-py==0.18.0 && \
    pip install runs==1.2.2 && \
    pip install s3transfer==0.10.1 && \
    pip install safetensors==0.4.3 && \
    pip install sagemaker==2.218.0 && \
    pip install schema==0.7.5 && \
    pip install setuptools==69.5.1 && \
    pip install six==1.16.0 && \
    pip install smdebug-rulesconfig==1.0.1 && \
    pip install sniffio==1.3.1 && \
    pip install starlette==0.37.2 && \
    pip install tblib==3.0.0 && \
    pip install tokenizers==0.19.1 && \
    pip install tqdm==4.66.4 && \
    pip install transformers==4.40.1 && \
    pip install typing-extensions==4.12.2 && \
    pip install tzdata==2024.1 && \
    pip install urllib3==2.2.1 && \
    pip install uvicorn==0.29.0 && \
    pip install uvloop==0.19.0 && \
    pip install watchfiles==0.21.0 && \
    pip install wcwidth==0.2.13 && \
    pip install websockets==12.0 && \
    pip install xmod==1.8.1 && \
    pip install xxhash==3.4.1 && \
    pip install yarl==1.9.4 && \
    pip install zipp==3.18.1 && \
    pip install httpx==0.28.1 && \
    pip install openai==1.58.1