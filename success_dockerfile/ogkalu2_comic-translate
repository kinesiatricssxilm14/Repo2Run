FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ogkalu2/comic-translate.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /comic-translate/. /repo && rm -rf /comic-translate/ && \
    rm -rf /comic-translate && \
    cd /repo && git checkout 1933d1ff3057d0852b08603aa973c62b9f559c74 && \
    pip install opencv_python==4.10.0.84 && \
    pip install PySide6==6.8.1 && \
    pip install dayu-path==0.5.2 && \
    pip install msgpack==1.1.0 && \
    pip install requests==2.32.3 && \
    pip install pymupdf==1.25.0 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install openai==1.57.0 && \
    pip install py7zr==0.22.0 && \
    pip install rarfile==4.2 && \
    pip install img2pdf==0.5.1 && \
    pip install EbookLib==0.18 && \
    pip install easyocr==1.7.2 && \
    pip install azure-ai-vision-imageanalysis==1.0.0 && \
    pip install deepl==1.20.0 && \
    pip install deep-translator==1.11.4 && \
    pip install stanza==1.9.2 && \
    pip install jaconv==0.4.0 && \
    pip install transformers==4.47.0 && \
    pip install wget==3.2 && \
    pip install ultralytics==8.3.40 && \
    pip install largestinteriorrectangle==0.2.1 && \
    pip install paddleocr==2.9.1 && \
    pip install paddlepaddle==2.6.2 && \
    pip install loguru==0.7.3 && \
    pip install google-generativeai==0.8.3 && \
    pip install anthropic==0.40.0 && \
    apt-get update -qq && \
    apt-get install libgl1-mesa-glx -y -qq && \
    apt-get update -qq && \
    apt-get install libxkbcommon0 -y -qq && \
    apt-get update -qq && \
    apt-get install libegl1 -y -qq && \
    apt-get update -qq && \
    apt-get install libdbus-1-3 -y -qq