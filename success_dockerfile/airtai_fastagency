FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/airtai/fastagency.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fastagency/. /repo && rm -rf /fastagency/ && \
    rm -rf /fastagency && \
    cd /repo && git checkout 1ff50361fff7665bd9c229a90aa1541ff243f667 && \
    cd /repo && pip install hatch==1.14.0 && \
    pip install fastapi==0.112 asyncer==0.0.8 websockets==13.0.0 && \
    pip install openai==1.57.4 && \
    pip install uvicorn==0.34.0 && \
    pip install pytest-asyncio==0.25.0 && \
    pip install requests==2.32.3 && \
    pip install fastapi-code-generator==0.5.2 datamodel-code-generator==0.25.6 && \
    pip install autogen[anthropic,together]==0.3.0 && \
    pip install bcrypt==4.2.1 mesop==0.12.7 && \
    pip install jsondiff==2.2.1 dirty-equals==0.8.0 && \
    pip install markdownify==0.14.1 firebase-admin==6.6.0 && \
    pip install passlib[bcrypt]==1.7.4 && \
    pip install python-multipart==0.0.20