FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/muchdogesec/history4feed.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /history4feed/. /repo && rm -rf /history4feed/ && \
    rm -rf /history4feed && \
    cd /repo && git checkout 61418241d9ab88d774bc0e57a7cd7f4e7b247810 && \
    pip install brotlipy==0.7.0 && \
    pip install click-plugins==1.1.1 && \
    pip install lxml-html-clean==0.4.1 && \
    pip install readability-lxml==0.8.1 && \
    pip install wcwidth==0.2.13 && \
    pip install fake-useragent==2.0.3 && \
    pip install whitenoise==6.7.0 && \
    pip install hyperlink==21.0.0 && \
    pip install Django==5.1.4 && \
    pip install djangorestframework==3.15.2 && \
    pip install drf_spectacular==0.28.0 && \
    pip install fake_useragent==2.0.3 && \
    pip install python-dotenv==1.0.1 && \
    pip install python_dateutil==2.8.2 && \
    pip install readability_lxml==0.8.1 && \
    pip install redis==5.2.1 && \
    pip install Requests==2.32.3