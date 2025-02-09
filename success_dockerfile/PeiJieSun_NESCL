FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/PeiJieSun/NESCL.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /NESCL/. /repo && rm -rf /NESCL/ && \
    rm -rf /NESCL && \
    cd /repo && git checkout 365d20d163024dfae5271da59a42b9ca074ace43 && \
    pip install torch==2.5.1 && \
    pip install numpy==1.22.4 && \
    pip install hyperopt==0.2.7 && \
    pip install pandas==2.2.3 && \
    pip install tqdm==4.67.1 && \
    pip install scikit_learn==1.6.0 && \
    pip install pyyaml==6.0.2 && \
    pip install colorlog==4.7.2 && \
    pip install colorama==0.4.4 && \
    pip install tensorboard==2.18.0 && \
    pip install cython==0.29.21 && \
    apt-get update -qq && \
    apt-get install -y -qq libblas-dev liblapack-dev gfortran && \
    pip install scipy==1.7.3 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    pip install -e /repo && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    apt-get update -qq && \
    apt-get install -y -qq python3-dev && \
    pip install numpy==1.22.4 -U --force-reinstall && \
    pip install numpy==1.22.3
ENV CFLAGS="-I/usr/local/lib/python3.10/site-packages/numpy/core/include"
ENV CFLAGS="-I/usr/local/lib/python3.10/site-packages/numpy/core/include -I/repo/recbole/util/cython/include"
RUN cd /repo/recbole/util/cython && python setup.py build_ext --inplace && \
    pip install numpy==1.22.4