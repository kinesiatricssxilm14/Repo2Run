FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lavague-ai/LaVague.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /LaVague/. /repo && rm -rf /LaVague/ && \
    rm -rf /LaVague && \
    cd /repo && git checkout b3557f8f350037e42acec5614135894796432c2c && \
    cd /repo && poetry lock && \
    cd /repo && poetry install
ENV PYTHONPATH="/repo/_lavague"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip install pillow==11.0.0
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip install trafilatura==2.0.0
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip install llama_index==0.12.8
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip install ipython==8.31.0
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip uninstall -y llama_index && \
    pip install llama-index==0.12.8
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip show llama-index && \
    python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/2.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/3.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip install jsonschema==4.23.0
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/6.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/7.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/8.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/9.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/10.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/11.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/12.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/13.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/14.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/15.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip install langchain==0.3.13
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/16.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/17.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/18.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/19.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/20.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/21.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/22.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/23.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/24.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/25.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/26.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/27.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/28.patch" && \
    python /code_edit.py -t "/search_patch/29.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/30.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/31.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN python /code_edit.py -t "/search_patch/32.patch"
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip install matplotlib==3.10.0
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"
RUN pip install msgpack==1.1.0
ENV PYTHONPATH="/repo/lavague-core:/repo/_lavague"