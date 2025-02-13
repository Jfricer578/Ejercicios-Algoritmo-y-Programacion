import time
import os

class Computadora:
    
    def __init__(self, marca, modelo, ram, procesador, almacenamiento, encendido):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.procesador = procesador
        self.almacenamiento = almacenamiento
        self.encendido = encendido

    def encender(self):
        if self.encendido == False:
            self.encendido = True
            print("Encendiendo la computadora...")
            time.sleep(1)
            print("La computadora está encendida")
        else:
            print("La computadora ya está encendida")
            time.sleep(1)

    def apagar(self):
        if self.encendido == True:
            self.encendido = False
            print("Apagando la computadora...")
            time.sleep(1)
            print("La computadora está apagada")
        else:
            print("La computadora ya está apagada")
            time.sleep(1)

    def actualizarRam(self, ram):
        if self.encendido == True:
            print("¿Por qué estás intentando cambiar la RAM con la computadora encendida?")
            time.sleep(1)
        elif self.encendido == False:
            print("Actualmente la computadora tiene", self.ram, "GB de RAM")
            self.ram = int(input("¿A cuánto quieres expandir la memoria RAM de la computadora? (en GB): "))
            print("La RAM se ha expandido a", self.ram, "GB")

    def actualizarAlmacenamiento(self, almacenamiento):
        if self.encendido == True:
            print("¿Por qué estás intentando cambiar el almacenamiento con la computadora encendida?")
            time.sleep(1)
        elif self.encendido == False:
            print("Actualmente la computadora tiene", self.almacenamiento, "GB de almacenamiento")
            self.almacenamiento = int(input("¿Cuanto almacenamiento tendrá la computadora? (en GB): "))
            print("El almacenamiento se ha actualizado a", self.almacenamiento, "GB")

    def verificarEstado(self):
        if self.encendido == True:
            print("La computadora está encendida\n")
        else:
            print("La computadora está apagada\n")

    def verComponentes(self):
        while True:
            os.system("cls")
            print("Marca:", self.marca)
            print("Modelo:", self.modelo)
            print("RAM:", self.ram, "GB")
            print("Procesador:", self.procesador)
            print("Almacenamiento:", self.almacenamiento, "GB")
            print("\n1. Volver")
            eleccion = int(input("Elija una opción (1): "))
            if eleccion == 1:
                break
            else:
                print("Opción inválida, vuelve a intentarlo")

laptop = Computadora("HP", "Pavilion", 8, "Intel Core i5", 256, False)

while True:
    time.sleep(1)
    os.system("cls")
    laptop.verificarEstado()
    print("¿Que hará la computadora?")
    print("1. Encender")
    print("2. Apagar")
    print("3. Actualizar RAM")
    print("4. Actualizar Almacenamiento")
    print("5. Ver componentes")
    print("6. Salir")

    eleccion = int(input("Elija una opción (1/2/3/4/5): "))
    if eleccion == 1:
        laptop.encender()
    elif eleccion == 2:
        laptop.apagar()
    elif eleccion == 3:
        laptop.actualizarRam(8)
    elif eleccion == 4:
        laptop.actualizarAlmacenamiento(256)
    elif eleccion == 5:
        laptop.verComponentes()
    elif eleccion == 6:
        print("La computadora se apagará automáticamente")
        if laptop.encendido == True:
            laptop.apagar()
            break
        else:
            break