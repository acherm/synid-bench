# Guesslang (deep-learning language guesser used by VS Code), pinned; TensorFlow 2.5 needs Python 3.8 on x86-64
FROM --platform=linux/amd64 python:3.8-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
