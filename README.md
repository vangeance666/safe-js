# Safe-JS

## Setup
### Docker
0. Install Docker for your operating system
[Link](`https://docs.docker.com/engine/install/`)__

1. Build image
```
➜ docker build -t safe-js .
```

2. Run container
```
➜ docker run -d --rm -p <desired_port>:80 --name <container-name> safe-js
```

2. Run container (With persistent storage using volume mount)
```
➜ docker run -d -rm -p <desired_port>:80 -v <your-mount-point>:/safe-js/save --name <container-name> safe-js
```

### Manual

0. Download and install Node.js 
[Link](`https://nodejs.org/en/`)

1. Install Box-JS with npm
```
➜ npm install box-js --global
```

2. Install Python 3.8 and above
[Link](`https://www.python.org/downloads/`)

3. Install dependencies
```
➜ pip install -r requirements.txt
```
4. Run
```
➜ python run.py
```

### Submit samples from your Browser

[Download Firefox extension here](https://github.com/vangeance666/safe-js-extension)



## Configurations
