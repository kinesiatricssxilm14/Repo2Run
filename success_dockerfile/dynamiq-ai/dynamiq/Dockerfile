FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/dynamiq-ai/dynamiq.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /dynamiq/. /repo && rm -rf /dynamiq/ && \
    rm -rf /dynamiq && \
    cd /repo && git checkout 6cca1ca29ebfe9517e61ddd7f2b54268ee025829 && \
    cd /repo && poetry install && \
    cd /repo && poetry install --with dev && \
    cd /repo && poetry install --with=dev && \
    pip install fakeredis==2.21.3 && \
    pip install litellm==1.55.4 && \
    pip install pymilvus==2.5.0 && \
    pip install psycopg==3.2.3 && \
    pip install pgvector==0.3.6 && \
    pip install qdrant-client==1.12.1 && \
    pip install weaviate-client==4.10.2 && \
    pip install jsonpath-ng==1.7.0 && \
    pip install jsonpickle==4.0.1 && \
    pip install filetype==1.2.0 && \
    pip install e2b==1.0.5 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch" && \
    python /code_edit.py -t "/search_patch/8.patch" && \
    python /code_edit.py -t "/search_patch/9.patch" && \
    python /code_edit.py -t "/search_patch/10.patch" && \
    python /code_edit.py -t "/search_patch/11.patch" && \
    python /code_edit.py -t "/search_patch/12.patch" && \
    python /code_edit.py -t "/search_patch/13.patch" && \
    python /code_edit.py -t "/search_patch/14.patch" && \
    python /code_edit.py -t "/search_patch/15.patch" && \
    python /code_edit.py -t "/search_patch/16.patch" && \
    python /code_edit.py -t "/search_patch/17.patch" && \
    python /code_edit.py -t "/search_patch/18.patch" && \
    python /code_edit.py -t "/search_patch/19.patch" && \
    python /code_edit.py -t "/search_patch/20.patch" && \
    python /code_edit.py -t "/search_patch/21.patch" && \
    python /code_edit.py -t "/search_patch/22.patch" && \
    python /code_edit.py -t "/search_patch/23.patch" && \
    python /code_edit.py -t "/search_patch/24.patch" && \
    python /code_edit.py -t "/search_patch/25.patch" && \
    python /code_edit.py -t "/search_patch/26.patch" && \
    python /code_edit.py -t "/search_patch/27.patch" && \
    python /code_edit.py -t "/search_patch/28.patch" && \
    python /code_edit.py -t "/search_patch/29.patch" && \
    python /code_edit.py -t "/search_patch/30.patch" && \
    python /code_edit.py -t "/search_patch/31.patch" && \
    python /code_edit.py -t "/search_patch/32.patch" && \
    python /code_edit.py -t "/search_patch/33.patch" && \
    python /code_edit.py -t "/search_patch/34.patch" && \
    python /code_edit.py -t "/search_patch/35.patch" && \
    python /code_edit.py -t "/search_patch/36.patch" && \
    python /code_edit.py -t "/search_patch/37.patch" && \
    python /code_edit.py -t "/search_patch/38.patch" && \
    python /code_edit.py -t "/search_patch/39.patch" && \
    python /code_edit.py -t "/search_patch/40.patch" && \
    pip install pytest-xdist==3.6.1 && \
    pip install python-pptx==1.0.2 && \
    pip install RestrictedPython==7.4 && \
    pip install pypdf==5.1.0 && \
    pip install unstructured-client==0.28.1