# ohcount (Black Duck's line counter; languages by extension, file name, Emacs mode line, shebang, libmagic,
# and content checks on shared extensions), Debian 13.7 package, pinned version
FROM debian:13.7-slim
RUN sed -i 's/^Types: deb$/Types: deb deb-src/' /etc/apt/sources.list.d/debian.sources \
      && apt-get update \
      && apt-get install -y --no-install-recommends ohcount=4.0.0-5 python3-minimal dpkg-dev xz-utils \
      && cd /tmp && apt-get source -q ohcount=4.0.0-5 \
      && grep -E '^#define LANG_' ohcount-4.0.0/src/languages.h | sed -E 's/.*"(.*)"/\1/' | sort -u > /labels.txt \
      && rm -rf /tmp/ohcount* && apt-get purge -y dpkg-dev xz-utils && apt-get autoremove -y \
      && rm -rf /var/lib/apt/lists/*
COPY identify.py /identify.py
ENTRYPOINT ["python3", "/identify.py"]
