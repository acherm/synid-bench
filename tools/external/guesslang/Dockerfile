# Guesslang (deep-learning language guesser used by VS Code), pinned. Guesslang 2.2.1 asks for TensorFlow 2.5,
# which has no ARM build and hangs under x86 emulation on Apple silicon; it runs here on TensorFlow 2.10.1
# (installed with --no-deps; same model files). All versions pinned in requirements.txt.
FROM python:3.10-slim
COPY requirements.txt /requirements.txt
RUN grep -v '^guesslang==' /requirements.txt > /deps.txt && pip install --no-cache-dir -r /deps.txt \
      && pip install --no-cache-dir --no-deps guesslang==2.2.1
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
