cadena = input("Ingrese una oración o frase: ")

def ContarPalabras(cadena):
    palabras = cadena.split()
    FrecuenciaPalabras = {}

    for palabra in palabras:
        if palabra in FrecuenciaPalabras:
            FrecuenciaPalabras[palabra] += 1
        else:
            FrecuenciaPalabras[palabra] = 1
    return FrecuenciaPalabras

FrecuenciaPalabras = ContarPalabras(cadena)

print("Frecuencia de palabras:")
for palabra, frecuencia in FrecuenciaPalabras.items():
    print(f"La palabra {palabra} aparece en la oración esta cantidad de veces: {frecuencia}")