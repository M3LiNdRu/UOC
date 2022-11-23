FROM node:lts-buster
WORKDIR /usr/src/app-server

COPY ./* ./
RUN npm install

CMD ["node", "index.js"]