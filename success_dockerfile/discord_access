FROM python:3.11
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/discord/access.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /access/. /repo && rm -rf /access/ && \
    rm -rf /access && \
    cd /repo && git checkout 19e9b1d5d295467c98f6a13fe43e4cdb5d7dfdd1 && \
    pip install click==8.1.7 && \
    pip install Flask==3.1.0 && \
    pip install Werkzeug==3.1.3 && \
    pip install gunicorn==23.0.0 && \
    pip install six==1.16.0 && \
    pip install python-dotenv==1.0.1 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install Flask-SQLAlchemy==3.1.1 && \
    pip install SQLAlchemy==2.0.36 && \
    pip install Flask-Migrate==4.0.7 && \
    pip install sqlalchemy-json==0.7.0 && \
    pip install cloud-sql-python-connector==1.14.0 && \
    pip install pg8000==1.31.2 && \
    pip install Flask-RESTful==0.3.10 && \
    pip install marshmallow==3.23.1 && \
    pip install marshmallow-sqlalchemy==1.1.0 && \
    pip install flask-marshmallow==1.2.1 && \
    pip install flask-apispec==0.11.4 && \
    pip install Flask-Cors==5.0.0 && \
    pip install flask-talisman==1.1.0 && \
    pip install PyJWT==2.10.1 && \
    pip install flask-oidc==2.2.2 && \
    pip install requests==2.32.3 && \
    pip install sentry-sdk[flask]==2.19.0 && \
    pip install okta==2.9.8 && \
    pip install pluggy==1.5.0 && \
    pip install tox==4.23.2 && \
    pip install ruff==0.8.0 && \
    pip install mypy==1.13.0 && \
    pip install types-google-cloud-ndb==2.3.0.20241103 && \
    pip install types-Flask-Cors==5.0.0.20240902 && \
    pip install types-Flask-Migrate==4.0.0.20240311 && \
    pip install types-python-dateutil==2.9.0.20241003 && \
    pip install types-requests==2.32.0.20241016 && \
    pip install pytest_factoryboy==2.7.0 && \
    pip install pytest_mock==3.14.0