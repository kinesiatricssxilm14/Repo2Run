FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/6abd/horus.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /horus/. /repo && rm -rf /horus/ && \
    rm -rf /horus && \
    cd /repo && git checkout c1d093e2090fc3817c924fc3ebae8c483744b7c5 && \
    pip install colorama==0.4.6 && \
    pip install cryptography==42.0.5 && \
    pip install Requests==2.32.2 && \
    pip install shodan==1.31.0 && \
    pip install pytest==8.1.1 && \
    pip install exif==1.6.0 && \
    pip install pytube==15.0.0 && \
    pip install pyshark==0.6 && \
    pip install python-nmap==0.7.1 && \
    pip install whois==1.20240129.2 && \
    pip install dnspython==2.6.1
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo
RUN mkdir -p /repo/src/modules/var/pipes && \
    touch /repo/src/modules/var/pipes/api_config.json
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo:/repo/src:$PYTHONPATH
RUN apt-get install -y -qq nmap && \
    pip install dhooks==1.1.4 hashcat==24.11.17 protonvpn-cli==2.2.11 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    pip install -e /repo
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo:/repo/src
RUN pip list && \
    pip install colorama==0.4.6 && \
    pip install cryptography==42.0.5 && \
    pip install Requests==2.32.2 && \
    pip install shodan==1.31.0 && \
    pip install pytest==8.1.1 && \
    pip install exif==1.6.0 && \
    pip install pytube==15.0.0 && \
    pip install pyshark==0.6 && \
    pip install python-nmap==0.7.1 && \
    pip install whois==1.20240129.2 && \
    pip install dnspython==2.6.1
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo:/repo/src
ENV PYTHONPATH=/repo:/repo/src
RUN python /code_edit.py -t "/search_patch/1.patch"
ENV PYTHONPATH=/repo:/repo/src
RUN python /code_edit.py -t "/search_patch/2.patch" && \
    python /code_edit.py -t "/search_patch/3.patch" && \
    python /code_edit.py -t "/search_patch/4.patch" && \
    python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch" && \
    python /code_edit.py -t "/search_patch/7.patch"
ENV PYTHONPATH=/repo:/repo/src
RUN python /code_edit.py -t "/search_patch/8.patch" && \
    python /code_edit.py -t "/search_patch/9.patch" && \
    python /code_edit.py -t "/search_patch/10.patch"
ENV PYTHONPATH=/repo:/repo/src
RUN python /code_edit.py -t "/search_patch/11.patch" && \
    python /code_edit.py -t "/search_patch/12.patch" && \
    python /code_edit.py -t "/search_patch/13.patch" && \
    python /code_edit.py -t "/search_patch/14.patch"
ENV PYTHONPATH=/repo:/repo/src
RUN python /code_edit.py -t "/search_patch/15.patch" && \
    python /code_edit.py -t "/search_patch/16.patch" && \
    python /code_edit.py -t "/search_patch/17.patch" && \
    python /code_edit.py -t "/search_patch/18.patch"
ENV PYTHONPATH=/repo:/repo/src
RUN python /code_edit.py -t "/search_patch/19.patch" && \
    python /code_edit.py -t "/search_patch/20.patch" && \
    python /code_edit.py -t "/search_patch/21.patch" && \
    python /code_edit.py -t "/search_patch/22.patch" && \
    python /code_edit.py -t "/search_patch/23.patch" && \
    python /code_edit.py -t "/search_patch/24.patch"
ENV PYTHONPATH=/repo:/repo/src
RUN cd /repo && pytest --collect-only -q