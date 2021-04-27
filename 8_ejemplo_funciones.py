def llamar ():
    print ("Llamaste a una función")
    print ("Puede tener texto", end = "")
    print (" con algo de formato", end = "\t")
    print ("que puede ser util")


def hola (nombre):
    print ("Un gusto en conocerte: ", nombre)

def potencia2 (num):
    return num**2


##########################################################################

print ("Llamar a una funcion: nombredefuncion()")
llamar()
input()

print ("Llamar a una funcion enviando parametro: nombredefuncion(par)")
nombre = input ("Escribe tu nombre: ")
hola (nombre)
input()

print ("Llamar a una funcion enviando parametro: nombredefuncion(par)")
hola (input ("Escribe tu nombre: "))
input()

print ("Llamar a una función enviando parametro y retornando valor")
resultado = potencia2 (int(input ("escribe tu valor")))
print (resultado)
input()

print ("Otra forma de hacerlo")
print ( potencia2(int(input ("escribe tu valor"))))
input()




lista = [0,5,10,15,20,25]
