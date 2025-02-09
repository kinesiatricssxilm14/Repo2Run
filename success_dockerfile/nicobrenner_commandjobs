FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/nicobrenner/commandjobs.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /commandjobs/. /repo && rm -rf /commandjobs/ && \
    rm -rf /commandjobs && \
    cd /repo && git checkout 4c72648b6858e85734c02a3c33b08c0f09ef1061 && \
    pip install beautifulsoup4==4.9.3 && \
    pip install requests==2.25.1 && \
    pip install openai==1.57.4 && \
    pip install python-dotenv==1.0.1 && \
    pip install selenium==4.25.0 && \
    pip install webdriver-manager==4.0.2
ENV PYTHONPATH=/repo/src
RUN python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH=/repo/src