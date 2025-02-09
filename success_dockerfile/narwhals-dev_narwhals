FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/narwhals-dev/narwhals.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /narwhals/. /repo && rm -rf /narwhals/ && \
    rm -rf /narwhals && \
    cd /repo && git checkout a2088f495a4725a1901b03621cc59a831af4c656 && \
    pip install tqdm==4.67.1 && \
    pip install covdefaults==2.3.0 && \
    pip install duckdb==1.1.3 && \
    pip install pandas==2.2.3 && \
    pip install polars==1.17.1 && \
    pip install pre-commit==4.0.1 && \
    pip install pyarrow==18.1.0 && \
    pip install pyarrow-stubs==2024.9.4 && \
    pip install pytest==8.3.4 && \
    pip install pytest-cov==6.0.0 && \
    pip install pytest-randomly==3.16.0 && \
    pip install pytest-env==1.1.5 && \
    pip install hypothesis==6.122.3 && \
    pip install hypothesis[numpy]==6.122.3 && \
    pip install scikit-learn==1.6.0 && \
    pip install typing_extensions==4.12.2