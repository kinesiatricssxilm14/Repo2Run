FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/erezsh/reladiff.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /reladiff/. /repo && rm -rf /reladiff/ && \
    rm -rf /reladiff && \
    cd /repo && git checkout d8683b232fe6b0ae2930c386c02cb43dd71bbff9 && \
    cd /repo && poetry install && \
    cd /repo && poetry show && \
    cd /repo && poetry install && \
    pip install parameterized==0.9.0 && \
    pip install click==8.1.7 && \
    pip install pandas==1.5.3 && \
    pip install parameterized==0.9.0 && \
    pip install plotly==5.9.0 && \
    pip install protobuf==5.29.1 && \
    pip install rich==13.9.4 && \
    pip install runtype==0.5.2 && \
    pip install sqeleton==0.1.6 && \
    pip install toml==0.10.2