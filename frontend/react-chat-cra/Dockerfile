FROM node:20

WORKDIR /frontend

COPY package*.json ./
RUN npm install --legacy-peer-deps
COPY .. .

CMD ["npm", "start"]
