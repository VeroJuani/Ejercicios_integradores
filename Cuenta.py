class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    def getTitular(self):
        return self.titular

    def setTitular(self, titular):
        self.titular = titular

    def getCantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

titular = input("Ingrese el titular de la cuenta: ")
cantidadInicial = float(input("Ingrese la cantidad inicial en la cuenta (opcional): ") or 0)

cuenta = Cuenta(titular, cantidadInicial)

cuenta.mostrar()

cantidadIngresar = float(input("Ingrese una cantidad para ingresar a la cuenta: "))
cuenta.ingresar(cantidadIngresar)

cuenta.mostrar()

cantidadRetirar = float(input("Ingrese una cantidad para retirar de la cuenta: "))
cuenta.retirar(cantidadRetirar)

cuenta.mostrar()