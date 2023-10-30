
trabajadores = {
    234566: ("Ingrid", 2008, "Estudiante", True),
    113567: ("Yoselin", 2006, "Estudiante", False),
    346788: ("Enzo", 2010, "Mecanico", False),
    632678: ("Miriam", 1986, "Gamer", True),
    987123: ("Pepe", 1990, "Gamer", True)
}

for trabajador in trabajadores:
    print(trabajadores[trabajador])

for trabajador in trabajadores:
    if 2008 in trabajadores[trabajador]:
        print(trabajador, "clave")    

for dni in trabajadores:
    print(f"DNI: {dni} >>>>>> {trabajadores[dni]}")        

    letras_mezcladas = ["a","v","F","S","e"]

for letra in letras_mezcladas:

  if letra in "aeiou":

    print(letra.upper())

  else:

    print("*")

    animal = {

  "nombre":"Luna",

  "edad":12

}

 

animal["edad"] = animal["edad"] + 3

print(animal["edad"])