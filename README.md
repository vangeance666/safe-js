# Safe-JS

## Setup
### Docker
0. Install Docker for your operating system
[here](https://docs.docker.com/engine/install/)

1. Build image
```
➜ docker build -t safe-js .
```

2. Run container
```bash
➜ docker run -d --rm -p <desired_port>:80 --name <container-name> safe-js
```

2. Run container (With persistent storage using volume mount)
```bash
➜ docker run -d -rm -p <desired_port>:80 -v <your-mount-point>:/safe-js/save --name <container-name> safe-js
```

### Docker-compose

1. Build and run the container using `docker-compose`
```bash
➜ docker-compose up -d
```

To stop and remove the container, simply run:

```bash
➜ docker-compose down
```



### Manual

0. Download and install Node.js 
[here](https://nodejs.org/en/)

1. Install Box-JS with npm
```bash
➜ npm install box-js --global
```

2. Download & Install Python 3.8 and above from
[here](https://www.python.org/downloads/)

3. Install dependencies
```bash
➜ pip install -r requirements.txt
```
4. Run
```bash
➜ python run.py
```

### Submit samples from your Browser

[Download Firefox extension here](https://github.com/vangeance666/safe-js-extension)
