# Rouge (Ruby syntax highlighter used by GitLab and Jekyll; Rouge::Lexer.guess), pinned with its Gemfile.lock
FROM ruby:3.3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN bundle config set --local frozen true && bundle install
COPY identify.rb ./
ENTRYPOINT ["bundle", "exec", "ruby", "/app/identify.rb"]
