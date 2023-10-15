cadena = "Son una cadena de texto para pruebas"

print(len(cadena))

print(cadena[1:])
print(cadena[3:16])
print(cadena[2:14:2])
print(cadena[2::3]) #cada 3 posiciones

#para ver los metodos
print(dir(cadena))
print(cadena.capitalize())
print(cadena.title()) #primeras letras de cada palabra en mayuscula
print(cadena.upper())
print(cadena.lower())
print(cadena.isalpha()) #preguntar si la cadena es alphanumerica o tiene espacios (false/true)
print("12".isdigit()) #pregunta si es un digito, numero

