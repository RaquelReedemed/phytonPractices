
#Tuplas, permite almacenar varios datos (no pueden ser modificar los valores)

mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)

print(mi_tupla[0])

#Listas, permite modificar los datos una vez creados

mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]

mi_lista.append('Nuevo Dato')
print(mi_lista)

#Asignacion multiple, asigna en una sola instruccion multiples variables

a,b,c = 'string', 15, True
print(a)
print(c)

#Guardar datos de entrada

""" entrada = input("Ingrese el valor que quiera guarda: ")
print(entrada) """

#Type: para saber el tipo de dato. Casting: para cambiar el tipo de dato

variable_1 = 5
print(type(variable_1))

variable_2 = str(variable_1)
print(type(variable_2))

numero = 4
while numero < 10:
    numero = numero - 1
    print("Hola")
 