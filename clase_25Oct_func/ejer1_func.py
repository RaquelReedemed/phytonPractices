
def generar_usuario(nombre, apellido):
    #TODO: Tomar la primera letra del nombre y agregar el apellido

    usuario = nombre[0].lower() + apellido.replace(" ", "").lower()
    return usuario

nom = input("Ingrese su nombre= ")
ape = input("Ingrese su apellido= ")

usu = generar_usuario(nom, ape)

print(f"Su nombre de usuario sera {usu}")