# danruizLSTI
# Librerias importadas Nmap
import sys 
import  argparse
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


def barra():
    bar2 = ChargingBar('Escanenado:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.1))
        bar2.next()
    bar2.finish()


def scan(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", dest="ip", help="Ingresa la ip de la victima")
    ip = parser.parse_args()
    # Se manda llamar el modulo portscan y se fuarda en la variable nm
    nm = nmap.PortScanner()
    # Se le solicita la ip al usuario
    # ip = input("[-] Ingresa la ip a scanear: --> ")
    # Se comienza a scanear la ip ingresada
    scaner = nm.scan(ip.ip)
    barra()
    count = 0
    puertos_abiertos = "-p"
    print("Host :  %s" % ip.ip)
    print("Stado : %s" % nm[ip.ip].state())
    # ciclo para listar todos los puertos de todos los protocolos UDP o TCP
    for protocolo in nm[ip.ip].all_protocols():
        print("Protocolo : %s" % protocolo)
        lport = nm[ip.ip][protocolo].keys()
        sorted(lport)
        for port in lport:
            print("Puerto : %s\tstate : %s" %
                  (port, nm[ip.ip][protocolo][port]["state"]))
            if count == 0:
                puertos_abiertos = puertos_abiertos+" "+str(port)
                count = 1
            else:
                puertos_abiertos = puertos_abiertos+","+str(port)
    print("Purtos abiertos: "+puertos_abiertos+" " + "--> "+str(ip.ip))


if __name__ == "__main__":
    print("Iniciando Scaneo")
    scan()
    
