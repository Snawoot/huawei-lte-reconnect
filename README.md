# huawei-lte-reconnect

Util to keep Huawei LTE modem/mobile router up 

## Install

```bash
mkdir -p ~/.venvs && \
python3 -m venv ~/.venvs/huawei-lte-api && \
~/.venvs/huawei-lte-api/bin/pip install -r requirements.txt && \
wget -O myip https://github.com/Snawoot/myip/releases/download/v1.2.0/myip.linux-amd64 && \
chmod +x myip
```

## Use

```
MYIP=./myip ./main_loop.sh ~/.venvs/huawei-lte-api/bin/python ./reconnect_dialup.py http://admin:PASSWORD@192.168.8.1/
```
