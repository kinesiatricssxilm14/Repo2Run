FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/huggingface/lighteval.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /lighteval/. /repo && rm -rf /lighteval/ && \
    rm -rf /lighteval && \
    cd /repo && git checkout 6ad7276e07efb3b383e6da42019f3e729c45a8e8 && \
    pip install transformers==4.47.1 && \
    pip install accelerate==1.2.1 && \
    pip install huggingface_hub==0.27.1 && \
    pip install gitpython==3.1.44 && \
    pip install datasets==3.2.0 && \
    pip install typer==0.9.4 && \
    pip install termcolor==2.3.0 && \
    pip install pytablewriter==1.2.1 && \
    pip install rich==13.9.4 && \
    pip install colorlog==6.9.0 && \
    pip install aenum==3.1.15 && \
    pip install nltk==3.9.1 && \
    pip install scikit-learn==1.6.0 && \
    pip install spacy==3.7.2 && \
    pip install sacrebleu==2.5.1 && \
    pip install rouge_score==0.1.2 && \
    pip install sentencepiece==0.2.0 && \
    pip install protobuf==3.20.3 && \
    pip install pycountry==24.6.1 && \
    pip install fsspec==2024.9.0 && \
    pip install torch==2.4.1 && \
    pip install numpy==1.26.4 && \
    pip install -e /repo
ENV PYTHONPATH=/repo
RUN pip install anyio==4.8.0 && \
    python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=/repo
RUN python -c "import lighteval.tasks.default_prompts as dp; print(dir(dp))" && \
    python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH=/repo
RUN python /code_edit.py -t "/search_patch/2.patch"
ENV PYTHONPATH=/repo
RUN python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch"
ENV PYTHONPATH=/repo
RUN python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch" && \
    python /code_edit.py -t "/search_patch/8.patch" && \
    python /code_edit.py -t "/search_patch/9.patch"
ENV PYTHONPATH=/repo
RUN python /code_edit.py -t "/search_patch/10.patch"
ENV PYTHONPATH=/repo
RUN python /code_edit.py -t "/search_patch/11.patch"
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q