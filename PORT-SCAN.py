# danruizLSTI
# Librerias importadas Nmap
import nmap
from progress.bar import Bar, ChargingBar
import os
import time
import random
print()
print("  _______    ________     ____      ____  ")
print(" |       \  /   _    \   /    \    /    \ ")
print(" |  |-|   ||   | |    | |      \__/     | ")
print(" |  |-|   ||   |_|    | |   |\     /|   | ")
print(" |_______/  \________/  |___| \___/ |___| ")
print()


print("[Info] Herramienta Para Escnear los puertos abiertos de un host")
print(" || Escrito totalmente en python usando libreria Nmap")
print(" || Creador de la Herramienta DanLSTI")
print()


def scan():
    # Se manda llamar el modulo portscan y se fuarda en la variable nm
    nm = nmap.PortScanner()
    # Se le solicita la ip al usuario
    ip = input("[-] Ingresa la ip a scanear: --> ")
    # Se comienza a scanear la ip ingresada
    scaner = nm.scan(ip)
    bar2 = ChargingBar('Instalando:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.2))
        bar2.next()
    bar2.finish()
    count = 0
    puertos_abiertos = "-p"
    print("Host :  %s" % ip)
    print("Stado : %s" % nm[ip].state())
    # ciclo para listar todos los puertos de todos los protocolos UDP o TCP
    for protocolo in nm[ip].all_protocols():
        print("Protocolo : %s" % protocolo)
        lport = nm[ip][protocolo].keys()
        sorted(lport)
        for port in lport:
            print("Puerto : %s\tstate : %s" %
                  (port, nm[ip][protocolo][port]["state"]))
            if count == 0:
                puertos_abiertos = puertos_abiertos+" "+str(port)
                count = 1
            else:
                puertos_abiertos = puertos_abiertos+","+str(port)
    print("Purtos abiertos: "+puertos_abiertos+" " + "--> "+str(ip))


scan()
