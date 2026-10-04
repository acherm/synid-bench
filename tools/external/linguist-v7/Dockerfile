# GitHub Linguist 7.30.0, the gem (Ruby), pinned with its dependencies by Gemfile.lock
FROM ruby:3.3-slim
RUN apt-get update && apt-get install -y --no-install-recommends build-essential cmake pkg-config libicu-dev \
      zlib1g-dev libcurl4-openssl-dev libssl-dev git && rm -rf /var/lib/apt/lists/*
COPY Gemfile Gemfile.lock /gems/
RUN cd /gems && BUNDLE_FROZEN=true bundle install
COPY identify.rb /identify.rb
ENTRYPOINT ["ruby", "/identify.rb"]
