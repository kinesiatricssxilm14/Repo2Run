FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/kennethreitz/simplemind.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /simplemind/. /repo && rm -rf /simplemind/ && \
    rm -rf /simplemind && \
    cd /repo && git checkout 39b5a5e19d536dcccb28df5ba245708884df74e5 && \
    pip install pydantic==2.10.3 && \
    pip install pydantic-settings==2.7.0 && \
    pip install instructor==1.7.0 && \
    pip install logfire==2.7.1