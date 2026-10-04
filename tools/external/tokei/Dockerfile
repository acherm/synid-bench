# tokei (line counter; recognises languages by file name, extension and, without an extension, shebang), pinned release
FROM rust:1.97.1-slim AS build
RUN cargo install tokei --version 15.0.0 --locked --root /out \
      && cp /usr/local/cargo/registry/src/*/tokei-15.0.0/languages.json /out/languages.json
FROM python:3.12-slim
COPY --from=build /out/bin/tokei /usr/local/bin/tokei
COPY --from=build /out/languages.json /languages.json
COPY identify.py /identify.py
ENTRYPOINT ["python", "/identify.py"]
