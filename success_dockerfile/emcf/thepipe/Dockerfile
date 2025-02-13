FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/emcf/thepipe.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /thepipe/. /repo && rm -rf /thepipe/ && \
    rm -rf /thepipe && \
    cd /repo && git checkout 02e397710bfae10a5b764c2b455d0d3697cb2376 && \
    pip install llama-index==0.10.50 && \
    pip install aiohttp==3.11.10 && \
    pip install charset-normalizer==3.4.0 && \
    pip install colorama==0.4.6 && \
    pip install requests==2.32.3 && \
    pip install pillow==10.4.0 && \
    pip install pydantic==2.10.3 && \
    pip install supabase==2.10.0 && \
    pip install markdownify==0.13.1 && \
    pip install magika==0.5.1 && \
    pip install scikit-learn==1.6.0 && \
    pip install python-dotenv==1.0.1 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install torchaudio==2.5.1 && \
    pip install docx2txt==0.8 && \
    pip install python-pptx==1.0.2 && \
    pip install pyarrow==18.1.0 && \
    pip install python-magic==0.4.27 && \
    pip install pandas==2.2.3 && \
    pip install pytesseract==0.3.13 && \
    pip install cssutils==2.11.1 && \
    pip install beautifulsoup4==4.12.3 && \
    pip install pymupdf==1.25.1 && \
    pip install pdf2image==1.17.0 && \
    pip install moviepy==2.1.1 && \
    pip install openpyxl==3.1.5 && \
    pip install pytube==15.0.0 && \
    pip install ffmpeg-python==0.2.0 && \
    pip install python-docx==1.1.2 && \
    pip install pymupdf4llm==0.0.17 && \
    pip install pytest-playwright==0.6.2 && \
    pip install playwright==1.49.1 && \
    pip install jwt==1.3.1 && \
    pip install sentence-transformers==3.3.1 && \
    pip install marker-pdf==1.1.0 && \
    pip install modal==0.68.25
RUN cd /repo && pytest --collect-only -q