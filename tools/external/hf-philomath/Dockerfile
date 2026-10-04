# philomath-1209/programming-language-identification (CodeBERTa-small fine-tuned on Rosetta Code, 26 languages),
# pinned: the model at a Hub commit (weights checked by sha256), baked in at build time (runs are offline);
# CPU-only torch and transformers pinned in requirements.txt (same base layers as the other hf-* tools).
FROM python:3.12-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r /requirements.txt
ARG REPO=philomath-1209/programming-language-identification
ARG REVISION=9090d38e7333a2c6ff00f154ab981a549842c20f
ARG WEIGHTS=model.safetensors
ARG SHA256=05db74cc2041bdc253966a9c5a171e767951baf7962dd6130b372cac04eb2dd3
RUN python -c "import sys; from huggingface_hub import snapshot_download as get; \
get(sys.argv[1], revision=sys.argv[2], local_dir='/model', allow_patterns=['*.json', '*.txt', sys.argv[3]], \
ignore_patterns=['onnx/*'])" "$REPO" "$REVISION" "$WEIGHTS" \
    && echo "$SHA256  /model/$WEIGHTS" | sha256sum -c - && rm -rf /model/.cache
ENV HF_HUB_OFFLINE=1 TRANSFORMERS_VERBOSITY=error OMP_NUM_THREADS=4 TOKENIZERS_PARALLELISM=false MAX_TOKENS=512
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
