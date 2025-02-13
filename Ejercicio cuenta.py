import random
import time
import os

def espera(tiempo):
    time.sleep(tiempo)
    os.system("cls")

def crearSaldoInicial():
    return random.randint(100, 1000)

def crearNumeroDeCuenta():
    numeroDeCuenta = ""
    for i in range(10):
        numeroDeCuenta += str(random.randint(0, 9))
    return numeroDeCuenta

class CuentaBancaria:

    def __init__(self, numeroDeCuenta, saldo):
        self.numeroDeCuenta = numeroDeCuenta
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo = self.saldo + monto
        print("Depósito exitoso")
        espera(2)

    def retirar(self, monto):
        if self.saldo < monto:
            print("Saldo insuficiente")
            espera(2)
        else:
            self.saldo = self.saldo - monto
            print("Retiro exitoso")
            espera(2)

    def mostrarSaldo(self):
        print("Su saldo actual es de:", self.saldo, "USD")
        espera(2.5)

cuenta1 = CuentaBancaria(crearNumeroDeCuenta(), crearSaldoInicial())

os.system("cls")
print("Bienvenido a su cuenta bancaria")

while True:
    print("Tu número de cuenta es:", cuenta1.numeroDeCuenta)
    print("¿Qué deseas hacer?")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo actual")
    print("4. Salir")

    eleccion = int(input("Elija una opción (1/2/3/4): "))
    if eleccion == 1:
        monto = float(input("Ingrese el monto para depositar: "))
        cuenta1.depositar(monto)
    elif eleccion == 2:
        monto = float(input("Ingrese el monto para retirar: "))
        cuenta1.retirar(monto)
    elif eleccion == 3:
        cuenta1.mostrarSaldo()
    elif eleccion == 4:
        print("Gracias por preferirnos")
        espera(2)
        break
    else:
        print("Opción inválida, vuelva a intentarlo")
        espera(2)