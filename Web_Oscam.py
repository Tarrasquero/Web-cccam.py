#!/usr/bin/env python
from requests.auth import HTTPDigestAuth
import requests
import os
from commands import getoutput
cccam = os.path.abspath(os.path.join(__file__, os.pardir, 'CCcam.cfg'))
cccam = open("CCcam.cfg", "r")
linea = cccam.readline()
server = getoutput('cat CCcam.cfg|grep "C:" | shuf -n1')
device = server.split(' ')
port = device[2]
user = device[3]
password = device[4]
device = device[1]
params = {"id": "server.config", "action": "execute",
          "label": "Reader-7", "protocol": "cccam",
          "device": device, "port": port,
          "user": user, "password": password, "action": "Save"
          }
url = 'http://192.168.1.56:8080/server_config.html?label=Reader-7' # Cambia la url por la de tu deco
r = requests.get(url, auth=HTTPDigestAuth('usuario', '0000'), params=params) # Cambia el "usuario" y "password"

print(r.status_code)
