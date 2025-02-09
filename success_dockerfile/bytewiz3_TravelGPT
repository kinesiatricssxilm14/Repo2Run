FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/bytewiz3/TravelGPT.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /TravelGPT/. /repo && rm -rf /TravelGPT/ && \
    rm -rf /TravelGPT && \
    cd /repo && git checkout b19b43095fd0343d7a0d045f59ec869c8b1fda33 && \
    pip install loguru==0.6.0 && \
    pip install pydantic==1.10.15 && \
    pip install PyJWT==2.8.0 && \
    pip install PyMySQL==1.1.0 && \
    pip install PyYAML==6.0.1 && \
    pip install SQLAlchemy==1.4.52 && \
    pip install fastapi==0.92.0 && \
    pip install openai==1.16.2 && \
    pip install starlette==0.25.0 && \
    pip install requests==2.31.0 && \
    pip install uvicorn==0.29.0 && \
    pip install httpx==0.27.2 && \
    pip install python-dotenv==1.0.1 && \
    pip install Jinja2==3.1.4 && \
    pip install sse-starlette==2.0.0 && \
    pip install redis==5.0.8 && \
    pip install pocode==0.0.3
ENV PYTHONPATH=$PYTHONPATH:/repo/common
RUN python /code_edit.py -t "/search_patch/0.patch"
ENV PYTHONPATH=$PYTHONPATH:/repo/common/utils
RUN python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH=$PYTHONPATH:/repo/common
RUN python /code_edit.py -t "/search_patch/2.patch"
ENV PYTHONPATH=$PYTHONPATH:/repo
RUN python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch"
ENV PYTHONPATH=/repo:$PYTHONPATH
RUN python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch" && \
    rm /repo/common/utils/email_utils.py && \
    python /code_edit.py -t "/search_patch/8.patch"
ENV PYTHONPATH=/repo:$PYTHONPATH