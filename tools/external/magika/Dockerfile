# Magika (Google; deep-learning content-type detection, from the bytes only), pinned
FROM python:3.12-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
