FROM node:16.11.1

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .
COPY package-lock.json .

# atualizar npm
RUN npm install
RUN npm install react-scripts@4.0.3 -g

COPY . .

EXPOSE 3000

RUN chown -R node:node /app/node_modules

CMD ["npm", "start"]
