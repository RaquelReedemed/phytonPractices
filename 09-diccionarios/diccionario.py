

dic1 = {
    "cuadrado": 4,
    "triangulo": 3,
    "rectangulo": 4,
    "hexagono": 6,
    "pentagono":5,
    "rombo": 4
}

""" coleccion=[(1,2), (33,87), ("Hola", True)]
print(coleccion)
dic1 = dict(coleccion) """

#obtener un valor segun su clave
print(dic1["hexagono"])

#modificar un valor segun su clave
dic1["hexagono"]=235
print(dic1["hexagono"])

#creando clave
dic1["hola"]=235

#agregando valores
dic1.update({"chau": 34, 37:12, "rombo":5})

#eliminar un elemento segun su clave
""" dic1.pop("hello") """

#cantidad de elementos
print(len(dic1))

#Pertenencia Si queremos saber si una clave o un valor estan en un diccionario

print("rombo" in dic1.keys(), "pertenenciaKeys")

print(3 in dic1.values(), "pertenenciaValor")



print(dic1) 

