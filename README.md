# pep-talk-generator  

Pep talk generator for those daily affirmations, written in python.

## Usage  

```bash
# clone the repo and change directories
git clone https://github.com/danieldupree/pep-talk-generator.git
cd pep-talk-generator

# Build
podman built -t pep-talk-generator:100 .
podman run --name pep-talk -p 5000:5000 pep-talk-generator:100
```

Goto [here](http://127.0.0.1:5000) press `F5` to 🔀. 😎
