FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/yihong1120/Construction-Hazard-Detection.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Construction-Hazard-Detection/. /repo && rm -rf /Construction-Hazard-Detection/ && \
    rm -rf /Construction-Hazard-Detection && \
    cd /repo && git checkout f5e1ca28d9999fd04c12a7ef30106b14410fa6db && \
    pip install aiofiles==24.1.0 && \
    pip install aiosqlite==0.20.0 && \
    pip install albumentations==1.4.21 && \
    pip install apscheduler==3.11.0 && \
    pip install asyncmy==0.2.9 && \
    pip install authlib==1.3.2 && \
    pip install bcrypt==4.2.0 && \
    pip install cloudinary==1.41.0 && \
    pip install codecov==2.1.13 && \
    pip install fastapi==0.115.5 && \
    pip install fastapi_jwt==0.3.0 && \
    pip install fastapi_limiter==0.1.6 && \
    pip install imagecorruptions==1.1.2 && \
    pip install imageio==2.35.1 && \
    pip install imgaug==0.4.0 && \
    pip install line-bot-sdk==3.14.2 && \
    pip install numpy==1.26.4 && \
    pip install onnx==1.17.0 && \
    pip install opencv_python==4.9.0.80 && \
    pip install opencv_python_headless==4.9.0.80 && \
    pip install Pillow==10.4.0 && \
    pip install pre-commit==4.0.1 && \
    pip install pycocotools==2.0.8 && \
    pip install pydantic_settings==2.6.1 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-xdist==3.6.1 && \
    pip install python-dotenv==1.0.1 && \
    pip install python-multipart==0.0.18 && \
    pip install python-socketio==5.11.4 && \
    pip install python-telegram-bot==21.7 && \
    pip install redis==5.2.0 && \
    pip install sahi==0.11.19 && \
    pip install schedule==1.2.2 && \
    pip install scikit-learn==1.5.2 && \
    pip install shapely==2.0.6 && \
    pip install speedtest-cli==2.1.3 && \
    pip install sqlalchemy[asyncio]==2.0.36 && \
    pip install streamlink==7.0.0 && \
    pip install streamlit==1.40.2 && \
    pip install tenacity==9.0.0 && \
    pip install torch==2.5.1 && \
    pip install torchvision==0.20.1 && \
    pip install twilio==9.3.7 && \
    pip install ultralytics==8.3.40 && \
    pip install uvicorn==0.32.1 && \
    pip install uvloop==0.21.0 && \
    pip install waitress==3.0.2 && \
    pip install watchdog==6.0.0 && \
    pip install werkzeug==3.1.3