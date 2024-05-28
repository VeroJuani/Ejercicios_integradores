print("Ingrese dos números para evaluar cual es su Minimo común múltiplo")

def CalcularMcd(a, b):
    while b:
        a, b = b, a % b
    return a

def CalcularMcm(a, b):
    mcd = CalcularMcd(a, b)
    return abs(a * b) // mcd


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

MinComMul = CalcularMcm(numero1, numero2)
print(f"El mínimo común múltiplo de {numero1} y {numero2} es {MinComMul}")