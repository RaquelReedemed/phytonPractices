
def contar_vocales(texto):
    #TODO: Contar las vocales
    cantidad_vocales = 0
    for x in texto:
        if x in "aeiou":
            cantidad_vocales +=1
    return cantidad_vocales

frase = input("Ingrese una frase: ")
cantidad = contar_vocales(frase)
print(f"La funcion tiene {cantidad} vocales")

