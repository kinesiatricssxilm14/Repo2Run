FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/betaacid/FastAPI-Reference-App.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /FastAPI-Reference-App/. /repo && rm -rf /FastAPI-Reference-App/ && \
    rm -rf /FastAPI-Reference-App && \
    cd /repo && git checkout 8caecad9d944a532a6e30bd9435bca9e978bd83c && \
    pip install fastapi==0.115.6 && \
    pip install uvicorn==0.34.0 && \
    pip install sqlalchemy==2.0.36 && \
    pip install alembic==1.14.0 && \
    pip install pydantic==2.10.3 && \
    pip install mock-alchemy==0.2.6 && \
    pip install pytest==8.3.4 && \
    pip install httpx==0.28.1 && \
    pip install requests==2.32.3 && \
    pip install python-dotenv==1.0.1 && \
    pip install psycopg2-binary==2.9.10 && \
    pip install responses==0.25.3
ENV DATABASE_URL="sqlite:///./test.db"