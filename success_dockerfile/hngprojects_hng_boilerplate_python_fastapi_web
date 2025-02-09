FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/hngprojects/hng_boilerplate_python_fastapi_web.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /hng_boilerplate_python_fastapi_web/. /repo && rm -rf /hng_boilerplate_python_fastapi_web/ && \
    rm -rf /hng_boilerplate_python_fastapi_web && \
    cd /repo && git checkout bc974027781b29b0dcee8d0cabaf00115fc620eb && \
    pip install aiohttp==3.9.5 && \
    pip install aiohttp-retry==2.8.3 && \
    pip install aiosignal==1.3.1 && \
    pip install aiosmtplib==2.0.2 && \
    pip install alembic==1.13.2 && \
    pip install annotated-types==0.7.0 && \
    pip install anyio==4.4.0 && \
    pip install astroid==3.2.4 && \
    pip install async-timeout==4.0.3 && \
    pip install attrs==23.2.0 && \
    pip install Authlib==1.3.1 && \
    pip install autopep8==2.3.1 && \
    pip install bcrypt==4.1.3 && \
    pip install black==24.4.2 && \
    pip install bleach==6.1.0 && \
    pip install blinker==1.8.2 && \
    pip install cachetools==5.4.0 && \
    pip install certifi==2024.7.4 && \
    pip install cffi==1.16.0 && \
    pip install cfgv==3.4.0 && \
    pip install charset-normalizer==3.3.2 && \
    pip install click==8.1.7 && \
    pip install colorama==0.4.6 && \
    pip install cryptography==43.0.0 && \
    pip install cssselect==1.2.0 && \
    pip install cssutils==2.11.1 && \
    pip install Deprecated==1.2.14 && \
    pip install dill==0.3.8 && \
    pip install distlib==0.3.8 && \
    pip install dnspython==2.6.1 && \
    pip install ecdsa==0.19.0 && \
    pip install email_validator==2.2.0 && \
    pip install exceptiongroup==1.2.2 && \
    pip install Faker==26.0.0 && \
    pip install fastapi==0.111.1 && \
    pip install fastapi-cli==0.0.4 && \
    pip install fastapi-mail==1.4.1 && \
    pip install filelock==3.15.4 && \
    pip install flake8==7.1.0 && \
    pip install frozenlist==1.4.1 && \
    pip install greenlet==3.0.3 && \
    pip install h11==0.14.0 && \
    pip install httpcore==1.0.5 && \
    pip install httptools==0.6.1 && \
    pip install httpx==0.27.0 && \
    pip install identify==2.6.0 && \
    pip install idna==3.7 && \
    pip install importlib_resources==6.4.4 && \
    pip install iniconfig==2.0.0 && \
    pip install isort==5.13.2 && \
    pip install itsdangerous==2.2.0 && \
    pip install Jinja2==3.1.4 && \
    pip install limits==3.13.0 && \
    pip install lxml==5.2.2 && \
    pip install Mako==1.3.5 && \
    pip install markdown-it-py==3.0.0 && \
    pip install MarkupSafe==2.1.5 && \
    pip install mccabe==0.7.0 && \
    pip install mdurl==0.1.2 && \
    pip install more-itertools==10.3.0 && \
    pip install multidict==6.0.5 && \
    pip install mypy-extensions==1.0.0 && \
    pip install nodeenv==1.9.1 && \
    pip install packaging==24.1 && \
    pip install passlib==1.7.4 && \
    pip install pathspec==0.12.1 && \
    pip install pillow==10.4.0 && \
    pip install pipdeptree==2.23.1 && \
    pip install platformdirs==4.2.2 && \
    pip install pluggy==1.5.0 && \
    pip install pre-commit==3.7.1 && \
    pip install premailer==3.10.0 && \
    pip install psycopg2-binary==2.9.9 && \
    pip install pyasn1==0.6.0 && \
    pip install pycodestyle==2.12.0 && \
    pip install pycparser==2.22 && \
    pip install pydantic==2.8.2 && \
    pip install pydantic-settings==2.3.4 && \
    pip install pydantic_core==2.20.1 && \
    pip install pyflakes==3.2.0 && \
    pip install Pygments==2.18.0 && \
    pip install PyJWT==2.8.0 && \
    pip install pylint==3.2.6 && \
    pip install PyMySQL==1.1.1 && \
    pip install pytest==8.2.2 && \
    pip install pytest-asyncio==0.23.8 && \
    pip install pytest-mock==3.14.0 && \
    pip install python-dateutil==2.9.0.post0 && \
    pip install python-decouple==3.8 && \
    pip install python-dotenv==1.0.1 && \
    pip install python-jose==3.3.0 && \
    pip install python-multipart==0.0.9 && \
    pip install pytz==2024.1 && \
    pip install PyYAML==6.0.1 && \
    pip install requests==2.32.3 && \
    pip install rich==13.7.1 && \
    pip install rsa==4.9 && \
    pip install shellingham==1.5.4 && \
    pip install six==1.16.0 && \
    pip install slowapi==0.1.9 && \
    pip install sniffio==1.3.1 && \
    pip install SQLAlchemy==2.0.31 && \
    pip install starlette==0.37.2 && \
    pip install stripe==10.7.0 && \
    pip install tomli==2.0.1 && \
    pip install tomlkit==0.13.0 && \
    pip install twilio==9.2.3 && \
    pip install typer==0.12.3 && \
    pip install typing_extensions==4.12.2 && \
    pip install urllib3==2.2.2 && \
    pip install uuid7==0.1.0 && \
    pip install uvicorn==0.30.3 && \
    pip install uvloop==0.19.0 && \
    pip install virtualenv==20.26.3 && \
    pip install watchfiles==0.22.0 && \
    pip install webencodings==0.5.1 && \
    pip install websockets==12.0 && \
    pip install wrapt==1.16.0 && \
    pip install yarl==1.9.4
ENV SECRET_KEY='your_secret_key_value'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587 MAIL_SERVER='your_mail_server'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token' TWILIO_PHONE_NUMBER='your_twilio_phone_number'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token' TWILIO_PHONE_NUMBER='your_twilio_phone_number' GOOGLE_CLIENT_ID='your_google_client_id'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token' TWILIO_PHONE_NUMBER='your_twilio_phone_number' GOOGLE_CLIENT_ID='your_google_client_id' GOOGLE_CLIENT_SECRET='your_google_client_secret'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token' TWILIO_PHONE_NUMBER='your_twilio_phone_number' GOOGLE_CLIENT_ID='your_google_client_id' GOOGLE_CLIENT_SECRET='your_google_client_secret' FRONTEND_URL='your_frontend_url'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='your_algorithm_value' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from@example.com' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token' TWILIO_PHONE_NUMBER='your_twilio_phone_number' GOOGLE_CLIENT_ID='your_google_client_id' GOOGLE_CLIENT_SECRET='your_google_client_secret' FRONTEND_URL='your_frontend_url'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='HS256' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from@example.com' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token' TWILIO_PHONE_NUMBER='your_twilio_phone_number' GOOGLE_CLIENT_ID='your_google_client_id' GOOGLE_CLIENT_SECRET='your_google_client_secret' FRONTEND_URL='your_frontend_url' MYSQL_DRIVER='your_mysql_driver'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='HS256' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='your_db_type' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from@example.com' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token' TWILIO_PHONE_NUMBER='your_twilio_phone_number' GOOGLE_CLIENT_ID='your_google_client_id' GOOGLE_CLIENT_SECRET='your_google_client_secret' FRONTEND_URL='your_frontend_url' MYSQL_DRIVER='pymysql'
ENV SECRET_KEY='your_secret_key_value' ALGORITHM='HS256' ACCESS_TOKEN_EXPIRE_MINUTES=30 JWT_REFRESH_EXPIRY=60 DB_HOST='your_db_host_value' DB_PORT=5432 DB_USER='your_db_user_value' DB_PASSWORD='your_db_password' DB_NAME='your_db_name' DB_TYPE='mysql' MAIL_USERNAME='your_mail_username' MAIL_PASSWORD='your_mail_password' MAIL_FROM='your_mail_from@example.com' MAIL_PORT=587 MAIL_SERVER='your_mail_server' FLUTTERWAVE_SECRET='your_flutterwave_secret' TWILIO_ACCOUNT_SID='your_twilio_account_sid' TWILIO_AUTH_TOKEN='your_twilio_auth_token' TWILIO_PHONE_NUMBER='your_twilio_phone_number' GOOGLE_CLIENT_ID='your_google_client_id' GOOGLE_CLIENT_SECRET='your_google_client_secret' FRONTEND_URL='your_frontend_url' MYSQL_DRIVER='pymysql'