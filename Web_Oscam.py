#!/usr/bin/env python
from requests.auth import HTTPDigestAuth
import requests
from lxml import html
from commands import getoutput
import time


class Lineas():
    def Reader1(self):
        try:
            self.last_line1 = getoutput(
                'cat CCcam.cfg|grep -e server.satunivers.tv|shuf -n1')
        except:
            self.last_line1 = getoutput(
                'cat CCcam.cfg|grep -e s2.cccam-free.com|shuf -n1')
        else:
        	self.last_line1 = getoutput(
                'cat CCcam.cfg|grep -e C:|shuf -n1')
        self.device1 = self.last_line1.split(' ')
        self.reader1 = ('Reader-1')
        device1 = self.device1[1]
        port1 = self.device1[2]
        user1 = self.device1[3]
        password1 = self.device1[4]
        self.paran = {"id": "server.config", "action": "execute",
                      "label": self.reader1, "protocol": "cccam",
                      "device": device1, "port": port1,
                      "user": user1, "password": password1,
                      "action": "Save"
                      }
        print self.paran
        self.http = 'http://192.168.1.xx:8080/server_config.html?label=Reader-1'
        self.url1 = (self.http)
        print self.url1
        self.recu = self.s.get(self.url1, auth=self.auth, params=self.paran)
        print self.recu.status_code

    def Reader2(self):
        try:
            self.last_line = getoutput(
                'cat CCcam.cfg|grep -e chzhbsqt.spyip.net|shuf -n1')
        except:
            self.last_line = getoutput(
                'cat CCcam.cfg|grep -e v1.fcnoip.org|shuf -n1')
        else:
        	self.last_line = getoutput(
                'cat CCcam.cfg|grep -e C:|shuf -n1')
        self.device = self.last_line.split(' ')
        self.reader2 = ('Reader-2')
        device = self.device[1]
        port = self.device[2]
        user = self.device[3]
        password = self.device[4]
        self.paran = {"id": "server.config", "action": "execute",
                      "label": self.reader2, "protocol": "cccam",
                      "device": device, "port": port,
                      "user": user, "password": password,
                      "action": "Save"
                      }
        print self.paran
        self.http2 = 'http://192.168.1.xx:8080/server_config.html?label=Reader-2'
        self.url = (self.http2)
        self.recu = self.s.get(self.url, auth=self.auth, params=self.paran)
        print self.recu.status_code

    def Comprobando(self):
        self.s = requests.Session()
        self.auth = HTTPDigestAuth('Tarrasquero', '0000')
        self.http = 'http://192.168.1.xx:8080/status.html'
        self.paran = {}
        self.recu = self.s.get(self.http, auth=self.auth, params=self.paran)
        self.tree = html.fromstring(self.recu.content)
        self.reader1 = self.tree.xpath(
            '//html/body/div[1]/div[2]/table/tbody[3]/tr[2]/td[12]/text()')
        self.reader2 = self.tree.xpath(
        	'//html/body/div[1]/div[2]/table/tbody[3]/tr[3]/td[12]/text()')
        if self.recu.status_code != 200:
            print('Acceso denegado')
            Micccam.Resfresco()
        else:
        	print('Comprobando Lineas')
        	Micccam.Actualizar()
    def Actualizar(self):
    	if 'CONNECTED' not in self.reader1:
            print('Actualizando card-1')
            time.sleep(5)
            Micccam.Reader1()
        else:
            print(str(self.reader1) + 'En card-1 No se hace nada')
        if 'CONNECTED' not in self.reader2:
            print('Actualizando card-2')
            time.sleep(5)
            Micccam.Reader2()
        else:
            print(str(self.reader2) + 'En card-2 No se hace nada')

Micccam = Lineas()
Micccam.Comprobando()

"""if __name__ == "__main__":
    cccam = os.path.abspath(os.path.join(__file__, os.pardir, 'myjob.log'))
    cccam = open(cccam, "a")
    cccam.write("Actualizado con exito\n")
    cccam.close()
"""
print "Fecha y hora " + time.strftime("%c")
