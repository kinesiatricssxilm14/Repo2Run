FROM python:3.10
WORKDIR /
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:$PATH"
RUN pip install pytest pytest-xdist && \
    pip install pipdeptree && \
    git clone https://github.com/lenML/Speech-AI-Forge.git && \
    mkdir /repo && \
    git config --global --add safe.directory /repo && \
    cp -r /Speech-AI-Forge/. /repo && rm -rf /Speech-AI-Forge/ && \
    rm -rf /Speech-AI-Forge && \
    cd /repo && git checkout 0b31b2238d994d07f54723f4f2dce4afb0fcdc44 && \
    pip install numpy==1.26.4 && \
    pip install scipy==1.14.1 && \
    pip install lxml==5.3.0 && \
    pip install pydub==0.25.1 && \
    pip install fastapi==0.115.6 && \
    pip install soundfile==0.12.1 && \
    pip install omegaconf==2.3.0 && \
    pip install pypinyin==0.53.0 && \
    pip install vocos==0.1.0 && \
    pip install pandas==2.2.3 && \
    pip install vector_quantize_pytorch==1.20.11 && \
    pip install einops==0.8.0 && \
    pip install transformers==4.41.2 && \
    pip install huggingface-hub==0.23.2 && \
    pip install tqdm==4.67.1 && \
    pip install python-ms==1.1.1 && \
    pip install datasets==3.2.0 && \
    pip install emojiswitch==0.0.3 && \
    pip install python-dotenv==1.0.1 && \
    pip install zhon==2.1.1 && \
    pip install mistune==3.0.2 && \
    pip install gradio==3.43.2 && \
    pip install gradio_client==0.5.0 && \
    pip install python-box==7.3.0 && \
    pip install ftfy==6.3.1 && \
    pip install librosa==0.10.2.post1 && \
    pip install pyrubberband==0.4.0 && \
    pip install pybase16384==0.3.7 && \
    pip install cachetools==5.5.0 && \
    pip install langdetect==1.0.9 && \
    pip install WeTextProcessing==1.0.4.1 && \
    pip install hydra-core==1.3.2 && \
    pip install loguru==0.7.3 && \
    pip install lightning==2.4.0 && \
    pip install natsort==8.4.0 && \
    pip install pyrootutils==1.0.4 && \
    pip install loralib==0.1.2 && \
    pip install wandb==0.19.1 && \
    pip install hyperpyyaml==1.2.2 && \
    pip install openai-whisper==20240930 && \
    pip install onnxruntime==1.20.1 && \
    pip install inflect==7.4.0 && \
    pip install matcha-tts==0.0.7.2 && \
    pip install faster_whisper==1.1.0 && \
    pip install pysubs2==1.7.3 && \
    pip install eng-to-ipa==0.0.2 && \
    pip install jieba==0.42.1 && \
    pip install cn2an==0.5.22 && \
    pip install lingua-language-detector==2.0.2 && \
    pip install torchdiffeq==0.2.5 && \
    pip install x-transformers==1.42.26 && \
    pip install ema-pytorch==0.7.7 && \
    pip install funasr==1.2.0 && \
    pip install jiwer==3.0.5 && \
    pip install zhconv==1.4.3 && \
    pip install moviepy==1.0.3 && \
    pip install modelscope==1.21.0 && \
    pip install onnx==1.17.0 && \
    pip install onnxconverter_common==1.14.0 && \
    pip install accelerate==1.2.1