FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/mbodiai/embodied-agents.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /embodied-agents/. /repo && rm -rf /embodied-agents/ && \
    rm -rf /embodied-agents && \
    cd /repo && git checkout 8715f674f16715f251f11538c183de44cf65b336 && \
    pip install hatchling==1.27.0 && \
    pip install anthropic==0.42.0 && \
    pip install art==6.4 && \
    pip install backoff==2.2.1 && \
    pip install datasets==3.2.0 && \
    pip install gymnasium==1.0.0 && \
    pip install h5py==3.12.1 && \
    pip install jsonref==1.1.0 && \
    pip install numpy==2.2.0 && \
    pip install openai==1.58.1 && \
    pip install pillow==11.0.0 && \
    pip install pydantic==2.10.4 && \
    pip install gradio==5.9.1 && \
    pip install gradio_client==1.5.2 && \
    pip install rich-click==1.8.5 && \
    pip install compress-pickle==2.1.0 && \
    pip install ruamel-yaml==0.18.6
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN pip install xarm-python-sdk==1.14.7 && \
    cd /repo && pip install -e .
RUN cd /repo && pytest --collect-only -q