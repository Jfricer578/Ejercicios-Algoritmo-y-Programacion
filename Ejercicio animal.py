import os
import time

def limpiarConsola():
    time.sleep(1.5)
    os.system("cls") 

class Animal:

    def __init__(self, nombre, edad, especie, sonido):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.sonido = sonido

    def hacerSonido(self):
        print(self.sonido)
        limpiarConsola()

    def cumplirAnios(self):
        self.edad += 1
        print(self.nombre, "cumplió un año, ahora tiene", self.edad, "años")
        limpiarConsola()
    
    def eleccion(self):
        while True:
            os.system("cls")
            print("Este es", self.nombre, "un", self.especie, "de", self.edad, "años")
            print("¿Que hará", self.nombre, "?")
            print("1. Hacer sonido")
            print("2. Cumplir años")
            print("3. Volver")
            eleccion = int(input("Elija una opción (1/2/3): "))
            if eleccion == 1:
                self.hacerSonido()
            elif eleccion == 2:
                self.cumplirAnios()
            elif eleccion == 3:
                limpiarConsola()
                break
            else:
                print("Opción inválida, vuelve a intentarlo")
                limpiarConsola()

perro = Animal("Tobby", 3, "Perro", "Guau!")
gato = Animal("Smithers", 2, "Gato", "Miau!")
Panda = Animal("Po", 1, "Panda", "Eso es ser barbaro")
loro = Animal("Rio", 1, "Loro","Bienvenidos")

while True:
    print("¿Que animal quieres ver?")
    print("1. Perro")
    print("2. Gato")
    print("3. Panda")
    print("4. Loro")
    print("5. Salir")

    eleccion = int(input("Elija una opción (1/2/3/4/5): "))
    if eleccion == 1:
        perro.eleccion()
    elif eleccion == 2:
        gato.eleccion()
    elif eleccion == 3:
        Panda.eleccion()
    elif eleccion == 4:
        loro.eleccion()
    elif eleccion == 5:
        break
    else:
        print("Opción inválida, vuelve a intentarlo")
        limpiarConsola()