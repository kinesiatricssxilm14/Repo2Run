FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/eakmanrq/sqlframe.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /sqlframe/. /repo && rm -rf /sqlframe/ && \
    rm -rf /sqlframe && \
    cd /repo && git checkout 61fda5dde52a8615019c863d76484cb2615ab0be && \
    pip install setuptools_scm==8.1.0 -U && \
    cd /repo && pip install -e . && \
    pip install pyspark==3.5.3 && \
    pip install duckdb==1.1.3 && \
    pip install findspark==2.0.1 && \
    pip install pytest_postgresql==6.1.1 && \
    pip install pytz==2024.2
RUN cd /repo && pytest --collect-only -q