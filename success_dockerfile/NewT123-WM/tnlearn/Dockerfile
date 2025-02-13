FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/NewT123-WM/tnlearn.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /tnlearn/. /repo && rm -rf /tnlearn/ && \
    rm -rf /tnlearn && \
    cd /repo && git checkout 50ee7596d2f77f0001d7d7c4a75e9d25528dbb63 && \
    pip install torch==2.5.1 && \
    pip install numpy==2.2.0 && \
    pip install scikit-learn==1.6.0 && \
    pip install pandas==2.2.3 && \
    pip install sympy==1.13.1 && \
    pip install tqdm==4.67.1 && \
    pip install matplotlib==3.10.0 && \
    pip install ipython==8.30.0 && \
    pip install torchinfo==1.8.0 && \
    pip install h5py==3.12.1 && \
    pip install setuptools==65.5.1 && \
    python /code_edit.py -t "/search_patch/0.patch"