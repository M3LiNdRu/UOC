# Oauth2App

This project was generated with NodeJS.

## Prerequisites

- Docker, Angular CLI and Nodejs
- Register Application through Linkedin Developers Portal
- Copy client_id and client_secret and paste it in the code

## Getting started

1- Clone the repository

$ git clone git@github.com:M3LiNdRu/UOC.git

2- Go to client app folder and build angular app

$ cd M1.770/PRAC1/oauth2-app-client
$ npm install
$ ng build

### 1st choice (Docker container)

3- Build docker image

$ docker build . -t oauth2-app-client

4- Run docker container

$ docker run -p 4200:4200 --add-host oauth-server:host-gateway -d oauth2-app-client

5- Go to server app folder and run express server app

$ cd ../oauth2-app-server
$ node index.js

6- Open your browser and browse to https://localhost:4200

7- Enjoy the journey!

### 2nd choice (using Docker compose) 

3- Go back to PRAC1 folder

$ cd ../

4- Run docker compose

$ docker-compose up -d

6- Open your browser and browse to https://localhost:4200

7- Enjoy the journey!





