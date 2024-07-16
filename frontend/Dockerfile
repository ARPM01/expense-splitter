FROM node:21.7.2

WORKDIR /expense-splitter-frontend

COPY package*.json ./

RUN npm install --force

COPY . .

RUN npm run build

RUN npm install -g serve

EXPOSE 3000

CMD ["serve", "-s", "build"]
