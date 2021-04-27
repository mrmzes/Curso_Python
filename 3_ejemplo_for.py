palabra = input("Escribe una palabra \n")
reversa = ""
#range() crea una secuencia de números
#range (start, stop, step)
#!Para recorrer inverso los pasos deben ser negativos
for i in range (len(palabra),0,-1):
    reversa +=palabra[i-1]
print (reversa)
