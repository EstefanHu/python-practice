# python-practice

### Python installation
- sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
- cd /tmp
- wget https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz
- tar -xf Python-3.12.2.tgz
- cd /Python-3.12.2.tgz
- ./configure --enable-optimizations
- make
- make test
- sudo make install

### pip3 installation
- sudo apt install python3-pip

### Virtual environments
- python -m venv `name`
- source `name`/bin/activate
- deactivate
- python -m pip freeze > requirenments.txt
- install -r

### Django installation
- python -m pip install Django

