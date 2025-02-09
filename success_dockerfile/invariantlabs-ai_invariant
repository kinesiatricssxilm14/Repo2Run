FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/invariantlabs-ai/invariant.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /invariant/. /repo && rm -rf /invariant/ && \
    rm -rf /invariant && \
    cd /repo && git checkout 81547a0d78a13951a6e415b9cd839d0ab68c6645 && \
    cd /repo/analyzer && pip install -e . && \
    ln -s /repo/testing/invariant/scorers /repo/testing/invariant/custom_types /repo/testing/invariant/testing /repo/analyzer/invariant/ && \
    pip install nltk==3.9.1 && \
    pip install invariant_sdk==0.0.4 && \
    pip install openai==1.58.1 && \
    cp -r /repo/testing/invariant/utils /repo/testing/invariant/constants.py /repo/analyzer/invariant/ && \
    cp -r /repo/testing/invariant/cache /repo/testing/invariant/manager.py /repo/testing/invariant/__main__.py /repo/analyzer/invariant/ && \
    pip install diskcache==5.6.3 && \
    cp /repo/testing/invariant/config.py /repo/analyzer/invariant/ && \
    python /code_edit.py -t "/search_patch/18.patch" && \
    python /code_edit.py -t "/search_patch/19.patch" && \
    python /code_edit.py -t "/search_patch/20.patch" && \
    python /code_edit.py -t "/search_patch/21.patch" && \
    pip install Pillow==11.0.0 && \
    cp /repo/testing/invariant/formatter.py /repo/analyzer/invariant/ && \
    pip install langchain_core==0.3.28 && \
    cp -r /repo/testing/invariant/wrappers /repo/analyzer/invariant/ && \
    pip install langchain_openai==0.2.14 && \
    pip install swarm && \
    pip install langgraph==0.2.60 && \
    pip list && \
    pip uninstall -y Swarm && \
    pip install swarm && \
    pip show -f swarm && \
    python /code_edit.py -t "/search_patch/22.patch" && \
    echo "try:\n from swarm import Swarm\n print('Swarm imported successfully')\n except Exception as e:\n print(str(e))" > /tmp/test_swarm_import.py && \
    echo "try:" > /tmp/test_swarm_import.py && \
    echo "    from swarm import Swarm" >> /tmp/test_swarm_import.py && \
    echo "    print('Swarm imported successfully')" >> /tmp/test_swarm_import.py && \
    echo "except Exception as e:" >> /tmp/test_swarm_import.py && \
    echo "    print(str(e))" >> /tmp/test_swarm_import.py && \
    python /tmp/test_swarm_import.py && \
    pip show swarm && \
    pip uninstall -y Swarm && \
    pip install openai-swarm==0.1.1