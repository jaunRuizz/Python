# Librerias importadas
import requests
import json
from bs4 import BeautifulSoup
from progress.bar import Bar, ChargingBar
import os
import time
import random
# Funcion que sirve para lozalizar una ip publica


def barra():
    bar2 = ChargingBar('Localizando:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.3))
        bar2.next()
    bar2.finish()


def localizador(ip):
    datos = []
    if ip is None:
        print("No se pudo localizar la ip")
        exit()
    else:
        rqst = requests.get('http://free.ipwhois.io/json/{}'.format(ip))
        sc = rqst.status_code
        if sc == 200:
            data = rqst.text
            data = json.loads(data)
            lat = str(data['latitude'])
            lon = str(data['longitude'])
            archivo = open("localizacion.txt", "w")
            for key in data:
                a = (key, ":", data[key])
                datos.append(a)
            for pas in datos:
                archivo.write(str(pas)+"\n")
            archivo.write('[+]' + ' Google Maps.................: ' +
                          'https://www.google.com/maps/place/' + lat + '+' + lon)
            archivo.close()
            print("Localizacion con exito ")
        else:
            print("API Fuera de servicio")
###################################################################################################################################################

# Funcion que sirve para obtener la ip publica de la victima


def my_ip():
    url1 = 'https://www.cual-es-mi-ip.net/'
    barra()
    # Peticiones a cada uno de los links
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.content,"html.parser")
    origen = soup1.find_all("span",class_="big-text font-arial")
    for i in origen:
        ip = i.text
    code = page1.status_code
    if code == 200:
        return ip
    else:
        ip = ''



if __name__=="__main__":
    ip = my_ip()
    localizador(ip)



