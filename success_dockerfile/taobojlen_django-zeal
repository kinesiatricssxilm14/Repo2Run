FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/taobojlen/django-zeal.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /django-zeal/. /repo && rm -rf /django-zeal/ && \
    rm -rf /django-zeal && \
    cd /repo && git checkout 232987c7ad3f33a1ad294fa2bd2dcb973e949cd2 && \
    pip install asgiref==3.8.1 && \
    pip install backports-tarfile==1.2.0 && \
    pip install build==1.2.1 && \
    pip install certifi==2024.6.2 && \
    pip install cffi==1.17.1 && \
    pip install charset-normalizer==3.3.2 && \
    pip install django==4.2.13 && \
    pip install django-stubs==5.0.2 && \
    pip install django-stubs-ext==5.0.2 && \
    pip install docutils==0.21.2 && \
    pip install exceptiongroup==1.2.2 && \
    pip install factory-boy==3.3.0 && \
    pip install faker==26.0.0 && \
    pip install filelock==3.16.1 && \
    pip install idna==3.7 && \
    pip install importlib-metadata==8.5.0 && \
    pip install iniconfig==2.0.0 && \
    pip install jaraco-classes==3.4.0 && \
    pip install jaraco-context==5.3.0 && \
    pip install jaraco-functools==4.0.1 && \
    pip install keyring==25.2.1 && \
    pip install markdown-it-py==3.0.0 && \
    pip install mdurl==0.1.2 && \
    pip install more-itertools==10.3.0 && \
    pip install nh3==0.2.17 && \
    pip install nodeenv==1.9.1 && \
    pip install packaging==24.1 && \
    pip install pkginfo==1.10.0 && \
    pip install pluggy==1.5.0 && \
    pip install pycparser==2.22 && \
    pip install pygments==2.18.0 && \
    pip install pyproject-hooks==1.1.0 && \
    pip install pyright==1.1.369 && \
    pip install pytest==8.2.2 && \
    pip install pytest-codspeed==3.0.0 && \
    pip install pytest-django==4.8.0 && \
    pip install pytest-mock==3.14.0 && \
    pip install pytest-random-order==1.1.1 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install readme-renderer==43.0 && \
    pip install requests==2.32.3 && \
    pip install requests-toolbelt==1.0.0 && \
    pip install rfc3986==2.0.0 && \
    pip install rich==13.9.4 && \
    pip install ruff==0.5.0 && \
    pip install six==1.16.0 && \
    pip install sqlparse==0.5.0 && \
    pip install tomli==2.1.0 && \
    pip install twine==5.1.1 && \
    pip install types-pyyaml==6.0.12.20240311 && \
    pip install typing-extensions==4.12.2 && \
    pip install urllib3==2.2.2 && \
    pip install zipp==3.21.0