FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/modelscope/agentscope.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /agentscope/. /repo && rm -rf /agentscope/ && \
    rm -rf /agentscope && \
    cd /repo && git checkout ceaf899339ce6ad421a4b5df85e009ae4738d5e5 && \
    pip install networkx==3.4.2 black==24.10.0 docstring_parser==0.16 pydantic==2.10.3 loguru==0.6.0 tiktoken==0.8.0 Pillow==11.0.0 requests==2.32.3 inputimeout==1.0.4 numpy==2.2.0 Flask==3.0.0 Flask-Cors==4.0.0 Flask-SocketIO==5.3.6 flask_sqlalchemy==3.1.1 flake8==7.1.1 psutil==6.1.0 scipy==1.14.1 openai==1.57.4 dashscope==1.20.14 && \
    pip install pytest==8.3.4 pytest-cov==6.0.0 pre-commit==4.0.1 sphinx==8.1.3 sphinx-autobuild==2024.10.3 sphinx_rtd_theme==3.0.2 myst-parser==4.0.0 sphinxcontrib-mermaid==1.0.0 transformers==4.47.0 && \
    pip install -e /repo && \
    pip install google==3.0.0 && \
    pip install cloudpickle==3.1.0 && \
    pip install protobuf==5.29.1