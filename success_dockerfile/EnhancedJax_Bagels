FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/EnhancedJax/Bagels.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Bagels/. /repo && rm -rf /Bagels/ && \
    rm -rf /Bagels && \
    cd /repo && git checkout d72d7fb5442f2b478741f1125a706fc9e3ad999e && \
    pip install freezegun==1.5.1 && \
    pip install sqlalchemy==2.0.36
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install pyyaml==6.0.2 && \
    pip install rich==13.9.4
ENV PYTHONPATH=$PYTHONPATH:/repo/src
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install xdg-base-dirs==6.0.2 && \
    pip install pydantic==2.10.3
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install pydantic-settings==2.7.0
ENV PYTHONPATH=$PYTHONPATH:/repo/src
RUN pip install pydantic-settings-yaml==0.2.0
ENV PYTHONPATH=$PYTHONPATH:/repo/src