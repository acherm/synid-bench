# cloc (counts lines; recognises languages by extension, file name and shebang), pinned release
FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends perl curl ca-certificates \
      && rm -rf /var/lib/apt/lists/* \
      && curl -fsSL -o /usr/local/bin/cloc https://github.com/AlDanial/cloc/releases/download/v2.10/cloc-2.10.pl \
      && chmod +x /usr/local/bin/cloc
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
