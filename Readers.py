#!/usr/bin/env python
import time
from requests.auth import HTTPDigestAuth
import requests
from lxml import html


def Comprobar():
    s = requests.Session()
    auth = HTTPDigestAuth('jorge', '0000')
    http = 'http://192.168.1.56:8080/status.html'
    paran = {}
    recu = s.get(http, auth=auth, params=paran)
    tree = html.fromstring(recu.content)
    connect = tree.xpath(
        '//html/body/div[1]/div[2]/table/tbody[3]/tr[2]/td[12]/text()')
    if 'CONNECTED' in connect:
        print('Todo bien en Card1')
        Comprobar2()
    else:
        import Card1
        Card1.Resfresco1()
        Comprobar()
    print "Fecha y hora " + time.strftime("%c")


def Comprobar2():
    s = requests.Session()
    auth = HTTPDigestAuth('jorge', '0000')
    http = 'http://192.168.1.56:8080/status.html'
    paran = {}
    recu = s.get(http, auth=auth, params=paran)
    tree = html.fromstring(recu.content)
    connect = tree.xpath(
        '//html/body/div[1]/div[2]/table/tbody[3]/tr[3]/td[12]/text()')
    if 'CONNECTED' in connect:
        print('Todo bien en Card2')
        Comprobar()
    else:
        import Card2
        Card2.Resfresco2()
        Comprobar2()
    print "Fecha y hora " + time.strftime("%c")


if __name__ == "__main__":
    Comprobar()
