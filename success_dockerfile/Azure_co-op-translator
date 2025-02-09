FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Azure/co-op-translator.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /co-op-translator/. /repo && rm -rf /co-op-translator/ && \
    rm -rf /co-op-translator && \
    cd /repo && git checkout a4709e4ad3ca224f3b319d62b2c8e63cd5b30e34 && \
    pip install annotated-types==0.7.0 && \
    pip install anyio==4.4.0 && \
    pip install appnope==0.1.4 && \
    pip install asttokens==2.4.1 && \
    pip install azure-ai-vision-imageanalysis==1.0.0 && \
    pip install azure-cognitiveservices-vision-computervision==0.9.1 && \
    pip install azure-common==1.1.28 && \
    pip install azure-core==1.30.2 && \
    pip install certifi==2024.6.2 && \
    pip install charset-normalizer==3.3.2 && \
    pip install click==8.1.7 && \
    pip install comm==0.2.2 && \
    pip install contourpy==1.2.1 && \
    pip install cycler==0.12.1 && \
    pip install decorator==5.1.1 && \
    pip install distro==1.9.0 && \
    pip install executing==2.0.1 && \
    pip install fonttools==4.53.1 && \
    pip install h11==0.14.0 && \
    pip install httpcore==1.0.7 && \
    pip install httpx==0.27.2 && \
    pip install idna==3.10 && \
    pip install isodate==0.6.1 && \
    pip install jedi==0.19.2 && \
    pip install kiwisolver==1.4.7 && \
    pip install matplotlib==3.9.4 && \
    pip install matplotlib-inline==0.1.7 && \
    pip install msrest==0.7.1 && \
    pip install numpy==1.25.2 && \
    pip install oauthlib==3.2.2 && \
    pip install openai==1.33.0 && \
    pip install opencv-python==4.10.0.84 && \
    pip install packaging==24.2 && \
    pip install parso==0.8.4 && \
    pip install pexpect==4.9.0 && \
    pip install pillow==10.3.0 && \
    pip install platformdirs==4.2.2 && \
    pip install prompt_toolkit==3.0.48 && \
    pip install psutil==5.9.8 && \
    pip install ptyprocess==0.7.0 && \
    pip install pure-eval==0.2.3 && \
    pip install pydantic==2.7.4 && \
    pip install pydantic_core==2.18.4 && \
    pip install pyparsing==3.1.4 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install python-dotenv==1.0.1 && \
    pip install pyyaml==6.0.2 && \
    pip install pyzmq==26.0.3 && \
    pip install requests==2.32.3 && \
    pip install requests-oauthlib==2.0.0 && \
    pip install semantic_kernel==1.8.3 && \
    pip install six==1.16.0 && \
    pip install sniffio==1.3.1 && \
    pip install stack-data==0.6.3 && \
    pip install tiktoken==0.7.0 && \
    pip install tornado==6.4.2 && \
    pip install tqdm==4.66.6 && \
    pip install traitlets==5.14.3 && \
    pip install typing_extensions==4.12.2 && \
    pip install urllib3==2.2.3 && \
    pip install wcwidth==0.2.13 && \
    pip install pytest==8.3.4 && \
    pip install ipykernel==6.29.5 && \
    pip install ipython==8.25.0 && \
    pip install jupyter_client==8.6.3 && \
    pip install jupyter_core==5.7.2 && \
    pip install nest-asyncio==1.6.0 && \
    pip install debugpy==1.8.11 && \
    pip install Pygments==2.18.0 && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1-mesa-glx