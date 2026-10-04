# @vscode/vscode-languagedetection (the Guesslang model in TensorFlow.js, as VS Code uses it), pinned with
# package-lock.json; the model files ship in the package (no network at run time)
FROM node:26.10.0-bookworm-slim
WORKDIR /tool
COPY package.json package-lock.json ./
RUN npm ci --omit=dev --ignore-scripts && npm cache clean --force
COPY identify.js ./
ENTRYPOINT ["node", "/tool/identify.js"]
