import os
import csv
import random

opcion1=True
trabajadores = [
   "Juan Pérez","María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
   "Laura Hernández", "Miguel Sánchez","Isabel Gómez", "Francisco Díaz","Elena Fernández"
                ]
sueldos=[["nombre trabajador","sueldo"]]
valorP=[]


def mediaGeometrica(data):
    producto=1
    for valor in data:
        producto*=valor
        return producto**(1/len(data))

def asignar_sueldos():
    for trabajador in trabajadores:
        sueldo=random([300000,2500000])
        sueldo.append(trabajador,sueldo)
        print("el sueldo se ha generado de manera exitosa")
        valorP.append(sueldo)
        for fila in sueldo:
            print(fila)


def clasificar_sueldos():
    sueldo_300=[["nombre","sueldo"]]
    sueldo_300y2000=[["nombre","sueldo"]]
    sueldo_2500=[["nombre","sueldo"]]
    for fila in sueldos[1:]:
        trabajador,sueldos=fila
        if sueldo < 30000:
            sueldo_300.append([fila])
        elif sueldo >=2000000:
            sueldo_300y2000.append([fila])
        elif sueldo_2500 >=2500000:
            sueldo_2500.append([fila])
    largoMnr=int(len( sueldo_300y2000))-1
    print(f"sueldo menor a $300.000{largoMnr}")
    for fila in sueldo_300:
        print(fila)
    largointr=int(len(sueldo_300y2000))-1
    print(f"sueldo entre 300.000 y 2.000.000 {largointr}")
    for fila in sueldo_300y2000:
        print(fila)    
    print(f"total de sueldos: {sum(valorP):0.2f}")    

def ver_estadisticas():
    maximo = max(valorP)
    minimo = min(valorP)
    total = sum(valorP)
    cantidad = len(valorP)
    promedio = total/cantidad
    print("el sueldo mas alto es: ${maximo} ")
    print("el sueldo mas bajo es: ${minimo} ")
    print("el sueldo promedio es: ${promedio} ")
    print("la media geometrica es  {mediaGeometrica(data)} ")

def reporte_sueldos():
    reporte=[["nombre","sueldo Base","descuento de Salud 7%","descuento afp 12%","sueldo liquido"]]
    nombre,sueldo = fila
    descafp=round(sueldo*0.7)
    descsalud=round(sueldo*0.12)
    liquido=sueldo-descafp-descsalud
    inforeport=[nombre,sueldo,descafp,descsalud,liquido]
    reporte.append(inforeport)
    for fila in reporte :
        print(f"{fila[0]:>15}{fila[1]:>15}{fila[3]:>15}{fila[4]:>15}")
    with open ("reporte_sueldos.csv","w",newline="") as reporte_csv:
        escritor_csv=csv.writer(reporte_csv)
        escritor_csv.writerows(reporte)    

def salir():
    print("saliendo del programa...")
    print("Desarrollado por robinson arriagada\nRut:16022537-8")
    opcion1=False
    

def menu():
    print("""
    Bienvenidos al registro de trabajadores y sueldos\n
    1. asignar sueldos aleatorios
    2. clasificar sueldos.
    3. ver estadisticas.
    4. reporte de sueldos
    5. salir del programa         

    """)
    try:
        opcion_menu=int(input("elija una opcion de menu :"))

 
        while opcion1:
                if opcion_menu==1:
                    asignar_sueldos()
                elif opcion_menu==2:
                   clasificar_sueldos()
                elif opcion_menu==3:
                    ver_estadisticas()
                elif opcion_menu==4:
                    reporte_sueldos()
                elif opcion_menu==5:
                        salir()
                else:
                    print(" ingrese una opcion valida ")
    except ValueError:
        print("ingrese una valor valido")
    

print(menu())

