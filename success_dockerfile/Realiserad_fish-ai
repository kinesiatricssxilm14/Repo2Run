FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/Realiserad/fish-ai.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /fish-ai/. /repo && rm -rf /fish-ai/ && \
    rm -rf /fish-ai && \
    cd /repo && git checkout f32c7f2eb75753c750ea264286b01fa26904c95b && \
    pip install iterfzf==1.4.0.54.3 && \
    pip install hugchat==0.4.17 && \
    pip install mistralai==1.2.5 && \
    pip install binaryornot==0.4.4 && \
    pip install anthropic==0.42.0 && \
    pip install openai==1.58.1 && \
    pip install protobuf==5.29.2 && \
    pip install simple_term_menu==1.6.6 && \
    pip install google-generativeai==0.8.3
RUN cd /repo && pytest --collect-only -q