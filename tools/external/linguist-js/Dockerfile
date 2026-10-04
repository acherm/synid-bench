# linguist-js (JavaScript re-implementation of GitHub Linguist's rules, without its classifier), pinned with
# package-lock.json; run offline on the Linguist data files bundled in the package
FROM node:26.10.0-bookworm-slim
WORKDIR /tool
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --ignore-scripts && npm cache clean --force
COPY identify.js ./
ENTRYPOINT ["node", "/tool/identify.js"]
