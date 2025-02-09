FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/shun-liang/yt2doc.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /yt2doc/. /repo && rm -rf /yt2doc/ && \
    rm -rf /yt2doc && \
    cd /repo && git checkout 201ec2929d82abad470883fd3c34bcd667914858 && \
    pip install hatch==1.14.0 && \
    pip install emoji==2.14.0 && \
    pip install faster-whisper==1.1.1 && \
    pip install ffmpeg-python==0.2.0 && \
    pip install instructor==1.7.2 && \
    pip install jinja2==3.1.5 && \
    pip install openai==1.59.5 && \
    pip install pathvalidate==3.2.3 && \
    pip install pydantic==2.10.4 && \
    pip install python-slugify==8.0.4 && \
    pip install torch==2.5.1 && \
    pip install tqdm==4.67.1 && \
    pip install typer-slim==0.15.1 && \
    pip install wtpsplit==2.1.2 && \
    pip install yt-dlp==2024.12.23 && \
    pip install ipython==8.31.0 && \
    pip install mypy==1.14.1 && \
    pip install pytest==8.3.4 && \
    pip install ruff==0.9.0 && \
    pip install types-tqdm==4.67.0.20241221
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN cd /repo && pytest --collect-only -q