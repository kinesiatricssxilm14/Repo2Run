FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/huchenlei/ComfyUI_omost.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /ComfyUI_omost/. /repo && rm -rf /ComfyUI_omost/ && \
    rm -rf /ComfyUI_omost && \
    cd /repo && git checkout 7ef00dd99450bd5e95b5e8da1524df98655cbc01 && \
    pip install transformers==4.41.2 && \
    pip install bitsandbytes==0.45.0 && \
    pip install protobuf==5.29.1 && \
    pip install torch==2.3.0 && \
    pip install openai==1.57.1 && \
    pip install requests==2.32.3 && \
    pip install comfy==0.0.1 && \
    pip install numpy==2.2.0 && \
    pip install openai==1.57.1 && \
    pip install Requests==2.32.3 && \
    pip install torch==2.3.0 && \
    pip install transformers==4.41.2 && \
    pip install typing_extensions==4.12.2 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch"