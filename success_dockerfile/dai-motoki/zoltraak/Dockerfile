FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/dai-motoki/zoltraak.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /zoltraak/. /repo && rm -rf /zoltraak/ && \
    rm -rf /zoltraak && \
    cd /repo && git checkout 4dce44df3fb2cd24822aecea941d15bd914c6374 && \
    pip install anthropic==0.40.0 && \
    pip install python-dotenv==1.0.1 && \
    pip install pyyaml==6.0.2 && \
    pip install graphviz==0.20.3 && \
    pip install groq==0.13.0 && \
    pip install pyperclip==1.9.0 && \
    pip install pytest==8.3.3 && \
    pip install tqdm==4.67.1 && \
    pip install loguru==0.7.2