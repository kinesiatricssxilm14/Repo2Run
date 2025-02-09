FROM python:3.10
WORKDIR /
COPY search_patch /search_patch
COPY code_edit.py /code_edit.py
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lucasdelimanogueira/PyNorch.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /PyNorch/. /repo && rm -rf /PyNorch/ && \
    rm -rf /PyNorch && \
    cd /repo && git checkout ed391e740c41806bf8e34265b8b1572b8f34d372 && \
    python /code_edit.py -t "/search_patch/0.patch" && \
    python /code_edit.py -t "/search_patch/1.patch" && \
    cd /repo && pip install -e . && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb && \
    apt-get update -qq && \
    apt-get install -y -qq wget && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    apt-get update -qq && \
    rm cuda-keyring_1.0-1_all.deb && \
    apt-get update && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin -qO - | tee /etc/apt/preferences.d/cuda-repository-pin-600 && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub && \
    apt-get update && \
    apt-get install -y -qq mlocate && \
    updatedb && \
    mkdir -p /usr/local/cuda/lib64 && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libcudnn8_8.1.0.77-1+cuda11.2_amd64.deb && \
    rm libcudnn8_8.1.0.77-1+cuda11.2_amd64.deb && \
    apt-get update && \
    apt-get install -y --no-install-recommends wget && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    apt-get update && \
    rm cuda-keyring_1.0-1_all.deb && \
    ldconfig && \
    apt-get remove -y --purge cuda* && \
    apt-get update && \
    ldconfig && \
    apt-get update && \
    apt-get install -y -qq software-properties-common && \
    apt-get update && \
    apt-get -f install && \
    apt-get update && \
    apt-get update && \
    ldconfig && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub && \
    apt-get update && \
    apt-get purge -y nvidia* && \
    apt-get update && \
    pip install torch==2.5.1 && \
    ln -s /usr/local/lib/python3.10/dist-packages/torch/lib/libcudart.so /usr/local/cuda/lib64/libcudart.so.12
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
RUN ldconfig && \
    ln -sf /usr/local/lib/python3.10/site-packages/nvidia/cuda_runtime/lib/libcudart.so.12 /usr/local/cuda/lib64/libcudart.so.12
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
RUN ldconfig && \
    apt-get install -y libopenmpi-dev
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
RUN ldconfig -v && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libnccl2_2.8.4-1+cuda11.0_amd64.deb && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libnccl-dev_2.8.4-1+cuda11.0_amd64.deb && \
    dpkg -i libnccl2_2.8.4-1+cuda11.0_amd64.deb && \
    dpkg -i libnccl-dev_2.8.4-1+cuda11.0_amd64.deb && \
    rm -f libnccl2_2.8.4-1+cuda11.0_amd64.deb libnccl-dev_2.8.4-1+cuda11.0_amd64.deb && \
    echo "/usr/local/cuda/lib64" > /etc/ld.so.conf.d/cuda.conf && \
    ldconfig && \
    pip install requests==2.32.3 && \
    pip install requests==2.32.3 && \
    pip install numpy==2.2.1 && \
    pip uninstall torch -y && \
    pip install torch==2.5.1 && \
    pip uninstall nvidia-nccl-cu12 -y && \
    pip install nvidia-nccl-cu12==2.21.5 && \
    pip uninstall torch -y && \
    pip install torch==2.5.1 && \
    apt-get update -qq && \
    apt-get install -y libnccl2 libnccl-dev && \
    apt-get purge -y libnccl2 libnccl-dev && \
    pip uninstall torch -y && \
    pip uninstall nvidia-nccl-cu12 -y && \
    pip install torch==2.5.1
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:/usr/local/cuda/lib64:$LD_LIBRARY_PATH
RUN ldconfig && \
    updatedb && \
    ln -s /usr/local/lib/python3.10/site-packages/nvidia/nccl/lib/libnccl.so.2 /usr/lib/x86_64-linux-gnu/libnccl.so.2 && \
    ldconfig && \
    pip install torchvision==0.20.1
RUN cd /repo && pytest --collect-only -q