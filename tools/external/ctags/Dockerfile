# Universal Ctags (tag generator; `--print-language` guesses a file's language from its name, shebang,
# modelines and a few content selectors), built from the pinned release
FROM debian:trixie-slim AS build
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl gcc make pkg-config \
      autoconf automake python3-docutils libjansson-dev libyaml-dev libxml2-dev libpcre2-dev \
      && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /src && curl -fsSL https://github.com/universal-ctags/ctags/archive/refs/tags/v6.2.1.tar.gz | tar -xz -C /src
WORKDIR /src/ctags-6.2.1
RUN ./autogen.sh && ./configure --prefix=/opt/ctags --disable-readcmd && make -j8 && make install
FROM debian:trixie-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 libjansson4 libyaml-0-2 libxml2 \
      libpcre2-8-0 && rm -rf /var/lib/apt/lists/*
COPY --from=build /opt/ctags /opt/ctags
COPY identify.py /identify.py
ENTRYPOINT ["python3", "/identify.py"]
