# scc (line counter; recognises languages by file name, extension, shebang, and keywords on shared extensions),
# pinned release binary, checked against the release's checksums.txt
FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
      && rm -rf /var/lib/apt/lists/* \
      && case "$(uname -m)" in \
           aarch64) a=arm64;  s=6e0d2a1f8d3540ba7df185477dec40bb7340f1b214bfd303147de5cad2bd7b8b ;; \
           x86_64)  a=x86_64; s=c7328436d3027f4357d3d7853f7dc3ac2bbcb4ca08f1adad91a27c593884079b ;; \
         esac \
      && curl -fsSL -o /tmp/scc.tgz https://github.com/boyter/scc/releases/download/v4.1.0/scc_Linux_$a.tar.gz \
      && echo "$s  /tmp/scc.tgz" | sha256sum -c - \
      && tar -xzf /tmp/scc.tgz -C /usr/local/bin scc && rm /tmp/scc.tgz
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
