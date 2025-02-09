FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/AdityaNG/kan-gpt.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /kan-gpt/. /repo && rm -rf /kan-gpt/ && \
    rm -rf /kan-gpt && \
    cd /repo && git checkout 0c6e4c2582d9a0e23c612c3b695846d4caceac1c && \
    pip install matplotlib==3.9.3 && \
    pip install numpy==2.1.3 && \
    pip install scikit_learn==1.5.2 && \
    pip install setuptools==65.5.1 && \
    pip install sympy==1.13.1 && \
    pip install torch==2.5.1 && \
    pip install tqdm==4.67.1 && \
    pip install pandas==2.2.3 && \
    pip install requests==2.32.3 && \
    pip install transformers==4.47.0 && \
    pip install wandb==0.19.0 && \
    pip install torchvision==0.20.1 && \
    pip install pytest==8.3.3 && \
    pip install coverage==7.6.8 && \
    pip install flake8==7.1.1 && \
    pip install black==24.10.0 && \
    pip install isort==5.13.2 && \
    pip install pytest-cov==6.0.0 && \
    pip install mypy==1.13.0 && \
    pip install gitchangelog==3.0.4 && \
    pip install mkdocs==1.6.1 && \
    pip install lark==1.2.2 && \
    pip install types-requests==2.32.0.20241016 && \
    pip install requests-mock==1.12.1
RUN cd /repo && pytest --collect-only -q