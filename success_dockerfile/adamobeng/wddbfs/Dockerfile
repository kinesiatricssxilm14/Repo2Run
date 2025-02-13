FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/adamobeng/wddbfs.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /wddbfs/. /repo && rm -rf /wddbfs/ && \
    rm -rf /wddbfs && \
    cd /repo && git checkout 5c68aabf647c313df7eb8c0371a5f9c3e88f7c03 && \
    pip install cheroot==10.0.1 && \
    pip install wsgidav==4.3.3 && \
    pip install configargparse==1.7 && \
    pip install pandas==2.2.3