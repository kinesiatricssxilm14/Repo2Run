FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/opengeos/HyperCoast.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /HyperCoast/. /repo && rm -rf /HyperCoast/ && \
    rm -rf /HyperCoast && \
    cd /repo && git checkout c1604cb53f3b917941c4105a157e4a1f0cb1b109 && \
    pip install dask==2024.12.0 && \
    pip install earthaccess==0.12.0 && \
    pip install geopandas==1.0.1 && \
    pip install h5netcdf==1.4.1 && \
    pip install hvplot==0.11.2 && \
    pip install leafmap==0.42.6 && \
    pip install localtileserver==0.10.5 && \
    pip install mapclassify==2.8.1 && \
    pip install netcdf4==1.7.2 && \
    pip install numpy==2.2.0 && \
    pip install psutil==6.1.0 && \
    pip install rioxarray==0.18.1 && \
    pip install s3fs==2024.10.0 && \
    pip install scikit-learn==1.6.0 && \
    pip install scipy==1.14.1 && \
    pip install xarray==2024.11.0 && \
    pip install black==24.10.0 && \
    pip install black[jupyter]==24.10.0 && \
    pip install build==1.2.2.post1 && \
    pip install bump-my-version==0.28.2 && \
    pip install cartopy==0.24.1 && \
    pip install click==8.1.7 && \
    pip install codespell==2.3.0 && \
    pip install fiona==1.10.1 && \
    pip install flake8==7.1.1 && \
    pip install ipykernel==6.29.5 && \
    pip install livereload==2.7.0 && \
    pip install mkdocs==1.6.1 && \
    pip install mkdocs-git-revision-date-localized-plugin==1.3.0 && \
    pip install mkdocs-git-revision-date-plugin==0.3.2 && \
    pip install mkdocs-jupyter==0.25.1 && \
    pip install mkdocs-material==9.5.49 && \
    pip install mkdocs-pdf-export-plugin==0.5.10 && \
    pip install mkdocstrings==0.27.0 && \
    pip install mkdocstrings-crystal==0.3.7 && \
    pip install mkdocstrings-python-legacy==0.2.4 && \
    pip install nbconvert==7.16.4 && \
    pip install nbformat==5.10.4 && \
    pip install openpyxl==3.1.5 && \
    pip install pygments==2.18.0 && \
    pip install pymdown-extensions==10.12 && \
    pip install pytest==8.3.4 && \
    pip install pytest-runner==6.0.1 && \
    pip install pyvista==0.44.2 && \
    pip install reuse==5.0.2 && \
    pip install seaborn==0.13.2 && \
    pip install sphinx==8.1.3 && \
    pip install torch==2.5.1 && \
    pip install twine==6.0.1 && \
    pip install watchdog==6.0.0 && \
    pip install wheel==0.44.0