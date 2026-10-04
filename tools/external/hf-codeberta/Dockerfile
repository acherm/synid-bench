# huggingface/CodeBERTa-language-id (CodeBERTa-small fine-tuned on CodeSearchNet, 6 languages), pinned: the model at
# a Hub commit (weights checked by sha256), baked in at build time (runs are offline); CPU-only torch and transformers
# pinned in requirements.txt (same base layers as the other hf-* tools).
FROM python:3.12-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r /requirements.txt
ARG REPO=huggingface/CodeBERTa-language-id
ARG REVISION=67e92a99a7979ff21a168fb147fcc464bfd2f82c
ARG WEIGHTS=pytorch_model.bin
ARG SHA256=4519a031ac532918a4b9b2ca9633d05e37ed3f68f52e7cf327ef94408d1d28a1
RUN python -c "import sys; from huggingface_hub import snapshot_download as get; \
get(sys.argv[1], revision=sys.argv[2], local_dir='/model', allow_patterns=['*.json', '*.txt', sys.argv[3]], \
ignore_patterns=['onnx/*'])" "$REPO" "$REVISION" "$WEIGHTS" \
    && echo "$SHA256  /model/$WEIGHTS" | sha256sum -c - && rm -rf /model/.cache
ENV HF_HUB_OFFLINE=1 TRANSFORMERS_VERBOSITY=error OMP_NUM_THREADS=4 TOKENIZERS_PARALLELISM=false MAX_TOKENS=512
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
