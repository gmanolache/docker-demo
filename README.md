# Docker demo

## 1. Standalone demo

Hello world style app using flask and docker

Building the image: 
```bash
docker build -t flask-app .
```

Running the image:

```bash
docker run -p 5000:5000 flask-app
```


## 2. Docker compose demo

Hello world style app using flask and docker and redis backed pgae hits counter

Running the stack:

```bash
docker-compose up
```

Stopping the stack

```bash
docker-compose up
```