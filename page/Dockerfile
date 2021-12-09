FROM node:16.11.1

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .
COPY package-lock.json .

# atualizar npm
RUN npm install --silent

COPY ./src/ ./src/
COPY ./public/ ./public/

EXPOSE 3000

CMD ["npm", "start"]
