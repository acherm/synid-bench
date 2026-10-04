# FrameByFrame/programming-language-identification-100plus (ModernBERT-base fine-tuned on Rosetta Code and The Stack
# v1, 107 languages), pinned: the model at a Hub commit (weights checked by sha256), baked in at build time (runs are
# offline); CPU-only torch and transformers pinned in requirements.txt (same base layers as the other hf-* tools).
# As the model card: the first 512 characters, eager attention. Weights are stored in bfloat16; run in float32.
FROM python:3.12-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r /requirements.txt
ARG REPO=FrameByFrame/programming-language-identification-100plus
ARG REVISION=da6a18b742571df3f01e4e8913ac27ac2283b4bf
ARG WEIGHTS=model.safetensors
ARG SHA256=52b6b9deceb722e8147f9115c0bf7ab8d7fa2a7a64ce6b63444bb82f8788e09d
RUN python -c "import sys; from huggingface_hub import snapshot_download as get; \
get(sys.argv[1], revision=sys.argv[2], local_dir='/model', allow_patterns=['*.json', '*.txt', sys.argv[3]], \
ignore_patterns=['onnx/*'])" "$REPO" "$REVISION" "$WEIGHTS" \
    && echo "$SHA256  /model/$WEIGHTS" | sha256sum -c - && rm -rf /model/.cache
ENV HF_HUB_OFFLINE=1 TRANSFORMERS_VERBOSITY=error OMP_NUM_THREADS=4 TOKENIZERS_PARALLELISM=false MAX_TOKENS=512 MAX_CHARS=512 ATTN=eager
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
