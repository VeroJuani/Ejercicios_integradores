print("Ingrese dos números para evaluar cual es su Máximo Común Divisor")

def CalcularMcd(a, b):
    while b:
        a, b = b, a % b
    return a


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

MaxComDiv = CalcularMcd(numero1, numero2)
print(f"El máximo común divisor de {numero1} y {numero2} es {MaxComDiv}")