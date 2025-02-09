FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/virattt/financial-datasets.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /financial-datasets/. /repo && rm -rf /financial-datasets/ && \
    rm -rf /financial-datasets && \
    cd /repo && git checkout 9856644262caab56cf174109924bba1d81330335 && \
    cd /repo && poetry install
ENV OPENAI_API_KEY='your_openai_api_key_here'
RUN cd /repo && poetry run pytest --collect-only -q