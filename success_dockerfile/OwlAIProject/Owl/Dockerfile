FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/OwlAIProject/Owl.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Owl/. /repo && rm -rf /Owl/ && \
    rm -rf /Owl && \
    cd /repo && git checkout 91922655c3cbf0e5f3282c22806b5ac0cf30063e && \
    apt-get update -qq && \
    apt-get install -y -qq portaudio19-dev && \
    cd /repo && poetry install && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    mkdir -p /repo/owl/services/transcription && \
    ln -s /repo/owl/services/stt/whisper_transcription_service.py /repo/owl/services/transcription/whisper_transcription_service.py && \
    python /code_edit.py -t "/search_patch/1.patch"
RUN cd /repo && poetry run pytest --collect-only -q