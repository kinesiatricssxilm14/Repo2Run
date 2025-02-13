FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/airbytehq/PyAirbyte.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /PyAirbyte/. /repo && rm -rf /PyAirbyte/ && \
    rm -rf /PyAirbyte && \
    cd /repo && git checkout 7e65ab3cfab39c04e6f0ece7cbc83367b7acb4a9 && \
    cd /repo && poetry install && \
    pip install pytest==8.3.4 && \
    pip install pytest-xdist==3.6.1 && \
    pip install sqlalchemy==2.0.35 && \
    pip install airbyte-cdk==6.11.1
ENV PYTHONPATH=/repo
RUN pip install pyarrow==17.0.0
ENV PYTHONPATH=/repo
RUN pip install airbyte-protocol-models==0.14.1
ENV PYTHONPATH=/repo
RUN pip install overrides==7.7.0
ENV PYTHONPATH=/repo
RUN pip install rich==13.9.4
ENV PYTHONPATH=/repo
RUN pip install structlog==24.4.0
ENV PYTHONPATH=/repo
RUN pip install -e /repo
ENV PYTHONPATH=/repo
RUN pip install docker==7.1.0
ENV PYTHONPATH=/repo
RUN pip install pytest-timeout==2.3.1
ENV PYTHONPATH=/repo
RUN pip install pdoc==15.0.1 viztracer==1.0.0 pytest-mock==3.14.0 responses==0.25.3 freezegun==1.5.1
ENV PYTHONPATH=/repo
RUN cd /repo && pytest --collect-only -q