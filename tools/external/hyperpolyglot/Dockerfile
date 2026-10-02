# Hyperpolyglot (Rust port of Linguist; Synid's heuristics and classifier come from it), pinned commit
FROM rust:1.90-slim AS build
RUN apt-get update && apt-get install -y --no-install-recommends git pkg-config && rm -rf /var/lib/apt/lists/*
WORKDIR /src
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN cargo build --release --locked
# its label set: the top-level keys of the languages.yml it was generated from
RUN f=$(ls /usr/local/cargo/git/checkouts/hyperpolyglot-*/*/languages.yml | head -1) \
      && grep -E '^[^ #][^:]*:[[:space:]]*$' "$f" | sed -E 's/:[[:space:]]*$//; s/^"(.*)"$/\1/' > /src/labels.txt
FROM debian:bookworm-slim
COPY --from=build /src/target/release/hyply-identify /usr/local/bin/hyply-identify
COPY --from=build /src/labels.txt /labels.txt
ENTRYPOINT ["hyply-identify"]
