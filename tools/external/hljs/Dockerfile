# highlight.js (syntax highlighter; highlightAuto over all its languages), pinned with package-lock.json
FROM node:26.10.0-bookworm-slim
WORKDIR /tool
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --ignore-scripts && npm cache clean --force
COPY identify.js ./
ENTRYPOINT ["node", "/tool/identify.js"]
