FROM python:3.9
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/jhj0517/AdvancedLivePortrait-WebUI.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /AdvancedLivePortrait-WebUI/. /repo && rm -rf /AdvancedLivePortrait-WebUI/ && \
    rm -rf /AdvancedLivePortrait-WebUI && \
    cd /repo && git checkout a7975cac39e3ab2573f52629df56a0f4d7521ecd && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install numpy==1.23.5 && \
    pip install opencv-python-headless==4.10.0.84 && \
    pip install imageio-ffmpeg==0.5.1 && \
    pip install lmdb==1.6.2 && \
    pip install timm==1.0.12 && \
    pip install rich==13.9.4 && \
    pip install albumentations==1.4.24 && \
    pip install ultralytics==8.3.58 && \
    pip install tyro==0.9.6 && \
    pip install dill==0.3.8 && \
    pip install gradio==4.44.1 && \
    pip install gradio-i18n==0.2.1 && \
    apt-get update -qq && \
    apt-get install -y -qq libgl1 && \
    pip install scikit-image==0.19.3 && \
    pip install moviepy==2.1.1 && \
    python -c "import moviepy; print(dir(moviepy))" && \
    pip uninstall -y moviepy && \
    pip install moviepy[optional]==2.1.1 && \
    pip uninstall -y moviepy && \
    pip install moviepy==2.1.1 && \
    pip install pillow==9.4.0 -U && \
    pip uninstall -y pillow && \
    pip install pillow==10.0 && \
    pip install moviepy==2.1.1 && \
    pip install gradio==4.44.1 && \
    pip uninstall -y moviepy && \
    pip install git+https://github.com/Zulko/moviepy.git && \
    python -c "from moviepy.video.io.VideoFileClip import VideoFileClip; print(VideoFileClip)" && \
    pip uninstall -y moviepy && \
    pip install -i https://mirrors.aliyun.com/pypi/simple moviepy==2.1.1 && \
    pip uninstall -y moviepy && \
    pip install moviepy==2.0.0 && \
    pip install dill==0.3.8 && \
    pip install ffmpeg==1.4 && \
    pip install gradio_i18n==0.2.1 && \
    pip install imageio==2.36.1 && \
    pip install insightface==0.7.3 && \
    pip install moviepy==2.1.1 && \
    pip install numpy==1.23.5 && \
    pip install Pillow==9.4.0 && \
    pip install pytest==7.1.2 && \
    pip install PyYAML==6.0 && \
    pip install Requests==2.32.3 && \
    pip install rich==13.9.4 && \
    pip install safetensors==0.5.1 && \
    pip install scikit_image==0.19.3 && \
    pip install torch==2.5.1 && \
    pip install tqdm==4.67.1 && \
    pip install ultralytics==8.3.58 && \
    pip uninstall -y moviepy && \
    pip install moviepy[optional]==2.1.1 && \
    pip uninstall -y moviepy && \
    pip install git+https://github.com/Zulko/moviepy.git@v2.1.1 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    pip uninstall -y scikit-image numpy && \
    pip install numpy==1.23.5 scikit-image==0.19.3 && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    pip uninstall -y moviepy && \
    pip install moviepy==2.1.1 -i https://mirrors.aliyun.com/pypi/simple && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    pip uninstall -y numpy scikit-image && \
    pip install numpy==1.23.5 scikit-image==0.19.3 && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    rm -f /usr/local/lib/python3.9/site-packages/moviepy/editor.py && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch"
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q