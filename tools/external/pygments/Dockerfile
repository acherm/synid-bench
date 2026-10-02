# Pygments (syntax highlighter; guess_lexer_for_filename / guess_lexer), pinned
FROM python:3.12-slim
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
