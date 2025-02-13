FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/illuin-tech/vidore-benchmark.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /vidore-benchmark/. /repo && rm -rf /vidore-benchmark/ && \
    rm -rf /vidore-benchmark && \
    cd /repo && git checkout 469665d6286f04a4ae09ed7c31dc66dfb44e727a && \
    pip install datasets==2.21.0 && \
    pip install tenacity==9.0.0 && \
    pip install transformers==4.47.0 && \
    pip install pytest==8.3.4 && \
    pip install ruff==0.8.3 && \
    pip install torch==2.5.1 && \
    pip install typer==0.15.1
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install scipy==1.14.1 && \
    pip install pillow==11.0.0 && \
    pip install pydantic==2.1.1
ENV PYTHONPATH=/repo:/repo/src
RUN pip install pytrec_eval==0.5 && \
    touch /repo/src/vidore_benchmark/__init__.py
ENV PYTHONPATH=/repo:/repo/src
RUN pip install mteb==1.25.1
ENV PYTHONPATH=/repo/src
RUN pip install python-dotenv==1.0.1 && \
    python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=/repo/src