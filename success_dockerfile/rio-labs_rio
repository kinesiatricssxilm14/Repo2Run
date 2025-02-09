FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/rio-labs/rio.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /rio/. /repo && rm -rf /rio/ && \
    rm -rf /rio && \
    cd /repo && git checkout eda40a731fb8a0ba6262fbee17eca3dcd4d5db4e
ENV PYTHONPATH=/repo
RUN pip install crawlerdetect==0.1.7 && \
    pip install fastapi==0.115.6 && \
    pip install fuzzywuzzy==0.18.0 && \
    pip install gitignore-parser==0.1.11 && \
    pip install imy[docstrings]==0.5.0 && \
    pip install introspection==1.9.2 && \
    pip install isort==5.13.2 && \
    pip install keyring==24.3.1 && \
    pip install langcodes==3.5.0 && \
    pip install narwhals==1.18.4 && \
    pip install ordered-set==4.1.0 && \
    pip install path-imports==1.1.2 && \
    pip install pillow==10.4.0 && \
    pip install python-levenshtein==0.26.1 && \
    pip install python-multipart==0.0.20 && \
    pip install pytz==2024.2 && \
    pip install revel==0.9.1 && \
    pip install timer-dict==1.0.0 && \
    pip install tomlkit==0.13.2 && \
    pip install typing-extensions==4.12.2 && \
    pip install unicall==0.1.5 && \
    pip install uniserde==0.3.14 && \
    pip install uvicorn[standard]==0.29.0 && \
    pip install watchfiles==0.24.0 && \
    pip install yarl==1.18.3
ENV PYTHONPATH=/repo
RUN pip install pyfakefs==5.7.3 && \
    pip install playwright==1.49.1 && \
    pip install numpy==2.2.0 && \
    pip install aiofiles==24.1.0
ENV PYTHONPATH=/repo
RUN pip install plotly==5.24.1 && \
    pip install matplotlib==3.10.0 && \
    pip install pandas==2.2.3
ENV PYTHONPATH=/repo
RUN pip install polars==1.17.1
ENV PYTHONPATH=/repo