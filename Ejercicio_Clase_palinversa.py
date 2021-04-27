palabra = input("Escribe una palabra: ")
lista = []
palinv = ''

for i in range (len(palabra)):
    lista.append(palabra[i])
lista.reverse()

for i in range (len(lista)):
    palinv += lista[i]
print (palinv)
