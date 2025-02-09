FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/codeskyblue/uiautodev.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /uiautodev/. /repo && rm -rf /uiautodev/ && \
    rm -rf /uiautodev && \
    cd /repo && git checkout eb8577b48bcf3dc524ccbdfc4bc7b0f0ba3e4862 && \
    cd /repo && poetry install
RUN cd /repo && poetry run pytest --collect-only -q