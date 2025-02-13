FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/ServiceNow/BrowserGym.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /BrowserGym/. /repo && rm -rf /BrowserGym/ && \
    rm -rf /BrowserGym && \
    cd /repo && git checkout c9aa9b134534f90b918517f065e5fb6ced398494 && \
    cd /repo && make install && \
    cd /repo && apt-get update -qq && \
    cd /repo && apt-get install -y -qq libnss3 libnspr4 libdbus-1-3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libxkbcommon0 libasound2 libatspi2.0-0
RUN cd /repo && pytest --collect-only -q