FROM node:16.15.0-alpine

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /usr/src/app/next
ADD /frontend/app/package.json package.json

RUN npm install
RUN yarn add -D prettier eslint-config-prettier eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
RUN yarn add axios swr 
RUN yarn add @mui/material @mui/lab
RUN yarn add @emotion/babel-plugin @emotion/react @emotion/styled


# サーバーの起動(nextアプリを作成した後、有効化する)。コンテナが起動してから30秒後くらいに起動。
# CMD ["yarn" "dev"]