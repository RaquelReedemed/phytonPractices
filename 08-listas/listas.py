

lista = ['hola', 1.4, 78, [10,20,30], False]

lista.append(234)
lista.append(23)
lista.insert(2, "chau")
lista.extend([10,20,40,99,"Hola"])

# .pop elimina el ultima elemento
""" lista.pop()
lista.pop(3) """

# .remove(), elimina pasandole el elemento a borrar
lista.remove("Hola")

# .count(), cuenta cuantas veces existe el elemento dentro de la lista
print(lista.count(78), "veces")

#concatenar 
lista1 = [1,2] + ["hola", True]

#longitud
print(len(lista1), "de longitud")

#pertenencia
print("Hola" in lista1)

#tipo
print(type(lista))

print(lista)