import os
import time

def espera():
    time.sleep(1.5)
    os.system("cls")

class Animal:

    def __init__(self, nombre, especie, sonido):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido

    def hacerSonido(self):
        print(self.nombre + ": " + self.sonido)

class Perro(Animal):

    def __init__(self, nombre, especie, sonido, raza):
        super().__init__(nombre, especie, sonido)
        self.raza = raza

perro1 = Perro("Toby", "Perro", "Guau!", "Schnauzer")
perro2 = Perro("Falco", "Perro", "Guau!", "Lobo Siberiano")

gato1 = Animal("Smithers", "Gato", "Miau!")

print("Estas son mis mascotas " + perro1.nombre + ", un " + perro1.raza + " y " + perro2.nombre + ", un " + perro2.raza + ", también tengo un gato llamado " + gato1.nombre)

while True:
    print("¿A quién quieres saludar?")
    print("1. Saludar a " + perro1.nombre)
    print("2. Saludar a " + perro2.nombre)
    print("3. Saludar a " + gato1.nombre)
    print("4. No saludar a ninguno")

    eleccion = int(input("Elige una opción: " ))
    if eleccion == 1:
        perro1.hacerSonido()
        espera()
    elif eleccion == 2:
        perro2.hacerSonido()
        espera()
    elif eleccion == 3:
        print("Es un gato, se acerca para que lo acaricies")
        espera()
    elif eleccion == 4:
        print("Te vas sin saludar a ningun animal")
        espera()
        break
    else:
        print("Opción inválida, vuelve a intentarlo")