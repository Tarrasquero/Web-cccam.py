#!/usr/bin/env python
from requests.auth import HTTPDigestAuth
import requests
from lxml import html
import time
import random


def Resfresco1():
    s = requests.Session()
    auth = HTTPDigestAuth('jorge', '0000')
    http = 'http://192.168.1.56:8080/status.html'
    paran = {}
    recu = s.get(http, auth=auth, params=paran)
    tree = html.fromstring(recu.content)
    connect = tree.xpath(
        '//html/body/div[1]/div[2]/table/tbody[3]/tr[2]/td[12]/text()')
    if recu.status_code != 200:
        print('Acceso denegado')
        paran = {"id": "shutdown.html",
                 "action": "Restart",
                 "Restart OSCam ?": "submit"
                 }
        http = ('http://192.168.1.56:8080/shutdown.html')
        s.get(http, auth=auth, params=paran)
    print('Comprobando Linea... ', connect)
    if 'CONNECTED' not in connect:
        ocurrencias = []
        f = open("CCcam.cfg", "r")
        lineas = f.readlines()
        f.close()
        f = open("CCcam.cfg", "w")
        for linea in lineas:
            if 'C:' in linea:
                f.write(linea)
        f.close()
        f = open("CCcam.cfg", "r")
        lineas = f.readlines()
        f.close()
        lineas = lineas[random.randint(0, len(lineas) - 1)]
        ocurrencias = lineas.split(' ')
        print ocurrencias
        device = ocurrencias[1]
        port = ocurrencias[2]
        user = ocurrencias[3]
        password = ocurrencias[4].rstrip('\n')
        paran = {"id": "server.config", "action": "execute",
                 "label": "Reader-1", "protocol": "cccam",
                 "device": device, "port": port,
                 "user": user, "password": password,
                 "action": "Save"
                 }
        print paran
        http = (
            'http://192.168.1.56:8080/server_config.html?label=Reader-1')
        recu = s.get(http, auth=auth, params=paran)
        print recu.status_code
        time.sleep(5)
        if 'CONNECTED' not in connect:
            print('Reintentando...  ')
            Resfresco1()
    else:
        print("Reader-1 Actualizado")


Resfresco1()

"""if __name__ == "__main__":
    cccam = os.path.abspath(os.path.join(__file__, os.pardir, 'myjob.log'))
    cccam = open(cccam, "a")
    cccam.write("Actualizado con exito\n")
    cccam.close()
"""
