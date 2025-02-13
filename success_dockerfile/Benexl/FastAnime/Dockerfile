FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Benexl/FastAnime.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /FastAnime/. /repo && rm -rf /FastAnime/ && \
    rm -rf /FastAnime && \
    cd /repo && git checkout 677f4690fab4651163d0330786672cf1ba1351bf && \
    echo "click>=8.1.7 inquirerpy>=0.3.4 pycryptodome>=3.21.0 pypresence>=4.3.0 requests>=2.32.3 rich>=13.9.2 thefuzz>=0.22.1 yt-dlp[default]>=2024.10.7" > /repo/requirements.txt && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    touch /repo/requirements-dev.txt && \
    pip install click==8.1.7 && \
    pip install inquirerpy==0.3.4 && \
    pip install pycryptodome==3.21.0 && \
    pip install pypresence==4.3.0 && \
    pip install requests==2.32.3 && \
    pip install rich==13.9.4 && \
    pip install thefuzz==0.22.1 && \
    pip install yt-dlp[default]==2024.12.13 && \
    pip install pre-commit==4.0.1 && \
    pip install pyinstaller==6.11.1 && \
    pip install pyright==1.1.390 && \
    pip install pytest==8.3.4 && \
    pip install ruff==0.8.3 && \
    pip install -e /repo