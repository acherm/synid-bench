# file(1) / libmagic from Debian 13 (trixie), pinned package version; Python only to write the JSON lines
FROM python:3.12.15-slim-trixie
RUN apt-get update && apt-get install -y --no-install-recommends file=1:5.46-5 libmagic1t64=1:5.46-5 \
      libmagic-mgc=1:5.46-5 && rm -rf /var/lib/apt/lists/*
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
