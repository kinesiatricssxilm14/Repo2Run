FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Toloka/dbt-af.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /dbt-af/. /repo && rm -rf /dbt-af/ && \
    rm -rf /dbt-af && \
    cd /repo && git checkout e7f436341f989bcdb070e2cbe76d61ed7d87f0f2 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q