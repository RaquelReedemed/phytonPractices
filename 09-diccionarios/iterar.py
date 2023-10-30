

dic1 = {
    "cuadrado": 4,
    "triangulo": 3,
    "rectangulo": 4,
    "hexagono": 6,
    "pentagono":5,
    "rombo": 4
}

#iterar sobre claves

for clave in dic1.keys():
    print(clave)

#iterar sobre valores

for valores in dic1.values():
    print(valores)

#iterar por clave y valores

for clave in dic1.keys():
    print(clave, dic1[clave])

#iterar por clave y valor, se itera sobre el metodo items()

for clave, valor in dic1.items():
    print(clave, valor)