lista_peliculas = [
    {
    "id": "3",
    "titulo": "Matrix"
}
]

pelicula = {
    "id": "4",
    "titulo": "Harry Potter"
}

lista_peliculas.append(pelicula)

for peli in lista_peliculas:
    if peli["titulo"] == "Matrix":
        peli["titulo"] = "Matrix 2"
print(lista_peliculas)   

for x in range(0, len(lista_peliculas)):
      #print(x)
      print(lista_peliculas[x])
      if lista_peliculas[x] == "Matrix 2":
           print(lista_peliculas[x])
           print(x)


for posicion in range(0, len(lista_peliculas)):
     if lista_peliculas[posicion]["titulo"] == "Matrix":
          print(lista_peliculas[posicion])
          print(posicion)
          break
pelicula_eliminada = lista_peliculas.pop(posicion)

print(lista_peliculas)
print("************")
print(pelicula_eliminada)