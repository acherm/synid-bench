# GitHub Linguist, the gem (Ruby), pinned
FROM ruby:3.3-slim
RUN apt-get update && apt-get install -y --no-install-recommends build-essential cmake pkg-config libicu-dev \
      zlib1g-dev libcurl4-openssl-dev libssl-dev git && rm -rf /var/lib/apt/lists/*
# its dependencies pinned too (the versions resolved on 2026-10-02)
RUN gem install --no-document charlock_holmes -v 0.7.9 && gem install --no-document rugged -v 1.9.6 \
      && gem install --no-document mini_mime -v 1.1.5 && gem install --no-document github-linguist -v 9.7.0
COPY identify.rb /identify.rb
ENTRYPOINT ["ruby", "/identify.rb"]
