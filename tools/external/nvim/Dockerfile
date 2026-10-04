# Neovim's filetype detection (vim.filetype.match), official release tarball pinned by checksum
FROM debian:13.7-slim
ARG TARGETARCH
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && rm -rf /var/lib/apt/lists/* \
    && case "$TARGETARCH" in \
         arm64) A=arm64; H=1aa5ca085249580ae0f91eb14f27ec0919773ff2d99a163d03f3d6c21ac29725 ;; \
         *) A=x86_64; H=bce0f56eda1f1b1db6eee8f4133d7a38813ea07933837dd1777411ca384c6875 ;; \
       esac \
    && curl -fsSL -o /tmp/nvim.tar.gz https://github.com/neovim/neovim/releases/download/v0.12.5/nvim-linux-$A.tar.gz \
    && echo "$H  /tmp/nvim.tar.gz" | sha256sum -c - \
    && tar -xzf /tmp/nvim.tar.gz -C /opt && mv /opt/nvim-linux-$A /opt/nvim && rm /tmp/nvim.tar.gz
COPY identify.lua /identify.lua
ENTRYPOINT ["/opt/nvim/bin/nvim", "--headless", "--clean", "-l", "/identify.lua"]
