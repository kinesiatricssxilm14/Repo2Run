FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/D4Vinci/Scrapling.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Scrapling/. /repo && rm -rf /Scrapling/ && \
    rm -rf /Scrapling && \
    cd /repo && git checkout 012820c6350282099219a5320196f46895f59c5a && \
    pip install -e /repo && \
    pip install autoscraper==1.1.14 pytest-httpbin==2.1.0 && \
    pip install mechanicalsoup==1.3.0 && \
    pip install parsel==1.9.1 && \
    pip install pyquery==2.0.1 && \
    pip install selectolax==0.3.27