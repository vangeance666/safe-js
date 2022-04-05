# Safe-JS

## What is this?
- 

## Running
### Docker

0. Install Docker for your operating system. Ref: `https://docs.docker.com/engine/install/` 

1. Build image
```
➜ docker build -t <image-tag> .
```

2. Run container
```
➜ docker run -it -rm -p 80:8090 --name <container-name> <image-tag>
```

2. Run container (With persistent storage using volume mount)
```
➜ docker run -it -rm -p 80:8090 -v <your-mount-point>:/safe-js/save --name <container-name> <image-tag>
```
docker run -it -p 8090:80 -v c:/Users/user/Desktop/save:/safe-js/save --name mybox safe-js


### Without Docker

0. Download and install Node.js `https://nodejs.org/en/`

1. Install Box-JS with npm
```
➜ npm install box-js --global
```

2. Install Python 3.8 and above `https://www.python.org/downloads/`

3. Install dependencies
```
➜ pip install -r requirements.txt
```
4. Run
```
➜ python run.py
```

### Submit using firefox extension

## Configurations
