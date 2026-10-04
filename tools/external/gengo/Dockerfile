# gengo (Rust re-implementation of Linguist's rules, without its classifier), pinned crate version
FROM rust:1.97.1-slim AS build
WORKDIR /src
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN cargo build --release --locked
# its label set: the top-level keys of the languages.yaml the crate is generated from
RUN grep -E '^[^ #-][^:]*:[[:space:]]*(#.*)?$' /usr/local/cargo/registry/src/*/gengo-language-0.15.0/languages.yaml \
      | sed -E 's/:[[:space:]]*(#.*)?$//; s/^"(.*)"$/\1/' > /src/labels.txt
FROM debian:13.7-slim
COPY --from=build /src/target/release/gengo-identify /usr/local/bin/gengo-identify
COPY --from=build /src/labels.txt /labels.txt
ENTRYPOINT ["gengo-identify"]
