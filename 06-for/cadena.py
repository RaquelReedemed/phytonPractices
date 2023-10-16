cadena = input("Ingrese una cadena: ")

vocales = 0


for letra in cadena:
    if letra in "aeiou":
        print("esta es vocal: ", letra) 
        vocales = vocales + 1 # tambiens e puede escribir vocales += 1
        print(vocales)
   # letra = vocales + 1


print(f"La cantidad de vocales en la cadena es de {vocales}")        
