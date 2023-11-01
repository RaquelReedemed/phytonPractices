
# *args se le indica a la funcion que puede agregar mas valres
def sumar(a, b, *args):
    """ print(a)
    print(b) """
    total = a + b
    for x in args:
        total = total + x 
    return total    
    

print(sumar(1, 2, 4, 5))  
#sumar(1,2,3) 