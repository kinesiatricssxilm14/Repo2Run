FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/beatzxbt/mm-toolbox.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /mm-toolbox/. /repo && rm -rf /mm-toolbox/ && \
    rm -rf /mm-toolbox && \
    cd /repo && git checkout 728e35dba7f13e5f9f349a4c7851faca98fff4ec && \
    pip install numpy==2.0.2 && \
    pip install mm_toolbox==0.2.1 && \
    pip install scipy==1.14.1