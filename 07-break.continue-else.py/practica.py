cadena = "Hola mundo una nueva clase estamos viendo"

for letra in cadena:
    if letra == "v":
        veces = cadena.count(letra)
        print(f"Letra encontrada y esta presente {veces} veces")
        break
else:
    print("letra no encontrada")

print("Fin")        