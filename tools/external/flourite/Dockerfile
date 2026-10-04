# flourite (regex-based snippet language detector, a fork of lang-detector; run on the first 10,000 characters),
# pinned with package-lock.json
FROM node:26.10.0-bookworm-slim
WORKDIR /tool
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --ignore-scripts && npm cache clean --force
COPY identify.js ./
ENTRYPOINT ["node", "/tool/identify.js"]
