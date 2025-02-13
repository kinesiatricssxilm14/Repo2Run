FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/WU-CVGL/BAD-Gaussians.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /BAD-Gaussians/. /repo && rm -rf /BAD-Gaussians/ && \
    rm -rf /BAD-Gaussians && \
    cd /repo && git checkout bdd8b3e2ba068aa7be8e3ab6fb5277abd40909bc && \
    pip install gsplat==1.4.0 && \
    pip install jaxtyping==0.2.36 && \
    pip install nerfstudio==1.1.5 && \
    pip install numpy==2.2.0 && \
    pip install pypose==0.6.9 && \
    pip install rich==13.9.4 && \
    pip install scipy==1.14.1 && \
    pip install torch==2.3.0 && \
    pip install typing_extensions==4.12.2 && \
    pip install viser==0.2.19
ENV PYTHONPATH=$PYTHONPATH:/repo