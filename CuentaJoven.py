class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular.nombre)
        print("Saldo:", self.cantidad)

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.cantidad:
                self.cantidad -= cantidad
            else:
                print("No hay suficiente saldo en la cuenta.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0):
        super().__init__(titular, cantidad)
        self.bonificacion = 5  # Bonificación del 5%

    def esTitularValido(self):
        edadMinima = 18
        edadMaximaJoven = 25
        return edadMinima <= self.titular.edad < edadMaximaJoven

    def mostrar(self):
        print("Tipo de cuenta: Cuenta Joven")
        print("Bonificación:", self.bonificacion, "%")


nombre = input("Ingrese el nombre del titular de la cuenta joven: ")
edad = int(input("Ingrese la edad del titular: "))
cantidadInicial = float(input("Ingrese la cantidad inicial en la cuenta joven: "))

titular = Persona(nombre, edad)
cuentaJoven = CuentaJoven(titular, cantidadInicial)

cuentaJoven.mostrar()

cantidadARetirar = float(input("Ingrese la cantidad a retirar: "))
cuentaJoven.retirar(cantidadARetirar)

print("Gracias por utilizar nuestra Cuenta Joven.")