FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/stephengpope/no-code-architects-toolkit.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /no-code-architects-toolkit/. /repo && rm -rf /no-code-architects-toolkit/ && \
    rm -rf /no-code-architects-toolkit && \
    cd /repo && git checkout ffc1a82547dbc188c5fbe4adb08ab55957f63e9f && \
    pip install Flask==3.1.0 && \
    pip install Werkzeug==3.1.3 && \
    pip install requests==2.32.3 && \
    pip install ffmpeg-python==0.2.0 && \
    pip install openai-whisper==20240930 && \
    pip install gunicorn==23.0.0 && \
    pip install APScheduler==3.11.0 && \
    pip install srt==3.5.3 && \
    pip install numpy==2.0.2 && \
    pip install torch==2.5.1 && \
    pip install google-auth==2.37.0 && \
    pip install google-auth-oauthlib==1.2.1 && \
    pip install google-auth-httplib2==0.2.0 && \
    pip install google-api-python-client==2.155.0 && \
    pip install google-cloud-storage==2.19.0 && \
    pip install psutil==6.1.0 && \
    pip install boto3==1.35.82 && \
    pip install Pillow==11.0.0