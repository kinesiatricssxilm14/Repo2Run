FROM python:3.11
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/StonyBrookNLP/appworld.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /appworld/. /repo && rm -rf /appworld/ && \
    rm -rf /appworld && \
    cd /repo && git checkout bc9c477c253beb2f410eff1a857444be9d5ae689 && \
    cd /repo && poetry install && \
    pip install pyperclip==1.9.0
ENV PYTHONPATH=/repo
ENV PYTHONPATH=/repo
RUN pip uninstall -y pyperclip && \
    pip install pyperclip==1.9.0
ENV PYTHONPATH=/repo
RUN python -c "import pyperclip; print(pyperclip.__version__)" && \
    cd /repo && poetry add pyperclip
ENV PYTHONPATH=/repo
RUN pip list && \
    cd /repo && poetry install
ENV PYTHONPATH=/repo
RUN cd /repo && poetry add psutil freezegun inflection fastapi && \
    cd /repo && poetry install
ENV PYTHONPATH=/repo
RUN cd /repo && poetry install --all-extras
ENV PYTHONPATH=/repo
ENV PYTHONPATH=/repo:/repo/scripts
RUN python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=/repo:/repo/scripts