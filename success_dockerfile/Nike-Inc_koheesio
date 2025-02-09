FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Nike-Inc/koheesio.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /koheesio/. /repo && rm -rf /koheesio/ && \
    rm -rf /koheesio && \
    cd /repo && git checkout 9bd29ec553cc6306520926a89d5e6405641b5994
ENV PYTHONPATH=/repo/src
RUN pip install jsonpickle==4.0.1
ENV PYTHONPATH=/repo/src
RUN pip install pyyaml==6.0.2
ENV PYTHONPATH=/repo/src
RUN pip install pydantic==2.10.3
ENV PYTHONPATH=/repo/src
RUN pip install pytest-order==1.3.0
ENV PYTHONPATH=/repo/src
RUN pip install aiohttp==3.11.10 && \
    pip install requests_mock==1.12.1 && \
    pip install pyspark==3.5.3 && \
    pip install delta-spark==3.2.1 && \
    pip install requests==2.32.3
ENV PYTHONPATH=/repo/src
RUN pip install aiohttp-retry==2.9.1 && \
    pip install pandas==2.2.3
ENV PYTHONPATH=/repo/src
RUN pip install nest_asyncio==1.6.0 && \
    pip install boxsdk==3.13.0 && \
    pip install chispa==0.10.1 && \
    pip install tableauhyperapi==0.0.20746 && \
    pip install tableauserverclient==0.34 && \
    pip install pyarrow==18.1.0 && \
    pip install paramiko==3.5.0
ENV PYTHONPATH=/repo/src
RUN python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH=/repo/src