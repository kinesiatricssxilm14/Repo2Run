FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/IAAR-Shanghai/Grimoire.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Grimoire/. /repo && rm -rf /Grimoire/ && \
    rm -rf /Grimoire && \
    cd /repo && git checkout 3fe89d2c9622fd6ef71a964a4a40aa11e2b069db && \
    pip install loguru==0.7.2 && \
    pip install requests==2.31.0 && \
    pip install openai==1.3.7 && \
    pip install sentence_transformers==2.2.2 && \
    pip install torch==2.1.1 && \
    pip install transformers==4.35.2 && \
    pip install tenacity==8.2.3 && \
    pip install accelerate==0.26.1 && \
    pip install numpy==2.2.0 && \
    pip install scipy==1.14.1 && \
    pip install scikit-learn==1.6.0 && \
    pip install matplotlib==3.10.0