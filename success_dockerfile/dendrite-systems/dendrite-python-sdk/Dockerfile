FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/dendrite-systems/dendrite-python-sdk.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /dendrite-python-sdk/. /repo && rm -rf /dendrite-python-sdk/ && \
    rm -rf /dendrite-python-sdk && \
    cd /repo && git checkout 27c9dab6baae53aabf65cf57615b6162397c64b2 && \
    cd /repo && poetry install && \
    cd /repo && poetry run playwright install && \
    cd /repo && apt-get update -qq && \
    cd /repo && apt-get install -y -qq libnss3 libnspr4 libdbus-1-3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2 libatspi2.0-0 && \
    # Check if the element exists by navigating and validating using cURL or a similar approach. curl -s https://browser-tests-alpha.vercel.app/api/download-test | grep "Download File" && \
    curl -o /dev/null --silent --head --write-out '%{http_code}\n' https://www.example.com
ENV PLAYWRIGHT_TIMEOUT=60000
RUN # Check if Playwright is functioning correctly with a simple script. echo "const { chromium } = require('playwright'); (async () => { const browser = await chromium.launch(); const page = await browser.newPage(); await page.goto('https://example.com'); console.log(await page.title()); await browser.close(); })();" > test_playwright.js && \
    cd /repo && mkdir -p playwright_logs
ENV PLAYWRIGHT_PERSISTENT_CONTEXT_LOG=1
ENV PLAYWRIGHT_CONTEXT_LOG=playwright_logs
ENV PLAYWRIGHT_DOWNLOADS=playwright_logs
RUN cd /repo && mkdir -p playwright_logs
ENV PLAYWRIGHT_PERSISTENT_CONTEXT_LOG=1
ENV PLAYWRIGHT_CONTEXT_LOG=playwright_logs
ENV PLAYWRIGHT_DOWNLOADS=playwright_logs
RUN python /code_edit.py -t "/search_patch/0.patch" && \
    cd /repo && poetry env info
ENV PYTHONPATH="/root/.cache/pypoetry/virtualenvs/dendrite-gW_DSdP6-py3.10/lib/python3.10/site-packages:/repo"
RUN cd /repo && pytest --collect-only -q