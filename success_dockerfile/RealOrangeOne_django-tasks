FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/RealOrangeOne/django-tasks.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /django-tasks/. /repo && rm -rf /django-tasks/ && \
    rm -rf /django-tasks && \
    cd /repo && git checkout e6d26ca2a233e86681b87c357d30af39f648dd9c && \
    pip install Django==5.1.4 typing_extensions==4.12.2 django-stubs-ext==5.1.1 ruff==0.8.3 coverage==7.6.9 django-stubs[compatible-mypy]==5.1.1 dj-database-url==2.3.0 mysqlclient==2.2.6 psycopg[binary]==3.2.3 && \
    cd /repo && pip install -e . && \
    cd /repo && python manage.py check && \
    cd /repo && python manage.py makemigrations --dry-run --check --noinput
ENV DJANGO_SETTINGS_MODULE=tests.settings
RUN python /code_edit.py -t "/search_patch/5.patch" && \
    python /code_edit.py -t "/search_patch/6.patch"
ENV DJANGO_SETTINGS_MODULE=tests.settings
RUN python /code_edit.py -t "/search_patch/7.patch" && \
    python /code_edit.py -t "/search_patch/8.patch" && \
    python /code_edit.py -t "/search_patch/9.patch" && \
    python /code_edit.py -t "/search_patch/10.patch" && \
    python /code_edit.py -t "/search_patch/11.patch" && \
    python /code_edit.py -t "/search_patch/12.patch" && \
    python /code_edit.py -t "/search_patch/13.patch" && \
    python /code_edit.py -t "/search_patch/14.patch" && \
    python /code_edit.py -t "/search_patch/15.patch"