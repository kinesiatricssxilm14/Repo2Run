FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/AuvaLab/itext2kg.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /itext2kg/. /repo && rm -rf /itext2kg/ && \
    rm -rf /itext2kg && \
    cd /repo && git checkout 941a1d1273831ca2e84930e6e5d8eb1117448f52 && \
    pip install langchain==0.3.0 && \
    pip install langchain-core==0.3.0 && \
    pip install langchain-openai==0.2.0 && \
    pip install neo4j==5.24.0 && \
    pip install numpy==1.26.4 && \
    pip install openai==1.45.0 && \
    pip install openpyxl==3.1.5 && \
    pip install pydantic-settings==2.5.2 && \
    pip install scikit-learn==1.5.2 && \
    pip install pypdf==4.3.1 && \
    pip install pytest==8.2.2
RUN cd /repo && pytest --collect-only -q