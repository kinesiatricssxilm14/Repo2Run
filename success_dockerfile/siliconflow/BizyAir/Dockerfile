FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/siliconflow/BizyAir.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /BizyAir/. /repo && rm -rf /BizyAir/ && \
    rm -rf /BizyAir && \
    cd /repo && git checkout cdb3bb86ab15216c78ad5c3097743c2a31582ab8 && \
    pip install oss2==2.19.1 && \
    pip install crcmod==1.7 && \
    pip install requests==2.32.3 && \
    pip install aiofiles==24.1.0 && \
    pip install aliyun-python-sdk-core==2.16.0 && \
    pip install aliyun-python-sdk-kms==2.16.5 && \
    pip install black==24.4.2 && \
    pip install isort==5.9.3 && \
    pip install pre-commit==4.0.1 && \
    pip install flake8==7.1.1 && \
    pip install aiohttp==3.11.10 && \
    pip install torch==2.5.1 && \
    pip install numpy==2.2.0 && \
    pip install pillow==11.0.0