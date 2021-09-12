# Dany ruiz
from datetime import date
from datetime import datetime
import random

# Esta funcion retorna la fecha actual


def date():
    fecha = datetime.now()
    año = fecha.year
    mes = fecha.month
    dia = fecha.day
    return año, mes, dia

# Esta funcion Retorna la edad actual que tienes


def mi_edad(año, mes, dia):
    # Esta parte del codigo valida que la fecha de nacimiento
    # sea la correcta
    f_nacimiento = int(input("En que año naciste "+" --> Ejemplo: (2019): "))
    while f_nacimiento > año or f_nacimiento < 1920:
        print("Error año no valido ", " ingresaste ", f_nacimiento, " El"
              " año tiene que estar entre 1920 y 2021 ")
        f_nacimiento = int(input("En que año naciste"
                                 "" + " --> Ejemplo: (2019): "))
    mes_nacimiento = int(input("En que mes naciste"
                               ""+" --> Ejemplo: (01): "))
    while mes_nacimiento > 12 or mes_nacimiento <= 0:
        print("Error mes no valido ", " ingresaste ", mes_nacimiento, " El"
              " mes tiene que estar entre 01 y 12 ")
        mes_nacimiento = int(input("En"
                                   " que mes naciste "+" --> Ejemplo: (01): "))
    dia_nacimiento = int(input("En que dia naciste "+" --> Ejemplo: (29): "))
    if mes == 2:
        while dia_nacimiento > 28 or dia_nacimiento <= 0:
            print("Error dia no valido ", " ingresaste ", dia_nacimiento, " El"
                  " dia tiene que estar entre 01 y 28 ")
            dia_nacimiento = int(input("En que dia"
                                       " naciste "+" --> Ejemplo: (29): "))
    else:
        while dia_nacimiento > 31 or dia_nacimiento <= 0:
            print("Error dia no valido ", " ingresaste ", dia_nacimiento, " El"
                  " dia tiene que estar entre 01 y 31 ")
            dia_nacimiento = int(input("En que"
                                       " dia naciste "+" --> Ejemplo: (29): "))
    if f_nacimiento < año or f_nacimiento > 1920:
        if mes_nacimiento <= 12 and mes_nacimiento > 0:
            if mes > mes_nacimiento:
                edad = año - f_nacimiento
                print("Tienes", edad, " Años")
            elif mes < mes_nacimiento:
                edad = año-f_nacimiento-1
                print("Tienes", edad, " Años")
            elif mes == mes_nacimiento:
                if dia < dia_nacimiento:
                    edad = año-f_nacimiento-1
                    print("Tienes", edad, " Años")
                elif dia > dia_nacimiento:
                    edad = año-f_nacimiento
                    print("Tienes", edad, " Años")
                elif dia == dia_nacimiento:
                    edad = año-f_nacimiento
                    print("Tienes", edad, " Años")
        return edad
    else:
        print("Error Año de nacimiento no valido")

# Esta funcion Retorna el tiempo que te queda de vida


def dia_muerte(edad, año):
    # Si la variable edad es nula
    # retorna error inesperado y se cierra el programa
    if edad is None:
        print("Fallo inesperado")
        exit()
    # Estamos usando la libreria random para sacar una fecha de muerte al azar
    dia_m = int((edad + 30)/3)
    day = random.randint(1, 31)
    mes = random.randint(1, 12)
    hora = random.randint(0, 24)
    minutes = random.randint(0, 60)
    años = random.randint(año, año+40)
    print("Te Restan: ", str(dia_m) + " Años ", str(mes)+" Me"
          "ses ", str(day)+" Dias ", str(hora)+" H"
          "oras ", str(minutes)+" Minutos "+" De vida ")

# Estamos usando main para dar
# jerarquia a cada una de las funciones que se van a ejecutar
if __name__ == "__main__":
    año, mes, dia = date()
    edad = mi_edad(año, mes, dia)
    dia_muerte(edad, año)
