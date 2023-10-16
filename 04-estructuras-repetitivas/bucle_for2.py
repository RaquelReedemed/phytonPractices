cantidad = 10

for numero in range(cantidad):
    if numero % 2 == 0:
        continue
    elif numero == 7:
        print("brack es igual a: ", numero)
        break
    else:
        print("numero vale ", numero)
else:
    print("finalizo el bucle y numero vale: ", numero)

print("fuera del bucle ")    
