
def contar_letras(texto, letras):

    #TODO: Contar letras
    cantidad = 0
    for x in texto:
        if x in letras:
            cantidad += 1
    return cantidad

frase = input("Input una frase: ")
letras = input("Que letras quiebre buscar: ")
cantidad = contar_letras(frase, letras) 
print(f"La funcion tiene {cantidad} letras buscadas")       
