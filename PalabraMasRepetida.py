cadena = input("Ingrese una oración o frase: ")

def ContarPalabras(cadena):
    palabras = cadena.split()
    FrecuenciaPalabras = {}

    for palabra in palabras:
        FrecuenciaPalabras[palabra] = FrecuenciaPalabras.get(palabra, 0) + 1

    return FrecuenciaPalabras

def PalabraMasRepetida(diccionario):
    PalabraMasRepetida = max(diccionario, key=diccionario.get)
    Frecuencia = diccionario[PalabraMasRepetida]
    return (PalabraMasRepetida, Frecuencia)


FrecuenciaPalabras = ContarPalabras(cadena)
PalabraRepetida, Frecuencia = PalabraMasRepetida(FrecuenciaPalabras)

print("Frecuencia de palabras:", FrecuenciaPalabras)
print("Palabra más repetida:", PalabraRepetida)
print("Frecuencia de la palabra más repetida:", Frecuencia)