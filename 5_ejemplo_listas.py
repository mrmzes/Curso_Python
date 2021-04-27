#UnaLista
miLista = [1,1,2,3,5,8]

print ("Ejemplo de una lista")
for elemento in range(len(miLista)):
    print (miLista[elemento])

input('presione enter')
for i in range(1,51,1):
    print(i)

input ("Ejemplo de una lista de elementos de varios tipos")
#Lista de varios elementos
otraLista = [1,1,2.0,"serie", 3, 10/2,4*2]

for elemento in otraLista:
    print ("\t",elemento, "\tes de tipo\t",type(elemento))

input ("Ejemplo de lista de listas")
#Lista de Listas
listaListas = [[1,1],[2,2],[3,3],["user","pass"]]

for lista in listaListas:
    print ("Lista: ",lista)
    for elemento in lista:
        print (elemento)
input ("Presiona Enter para continuar...")
#slicing

print ("Ejemplo de Slicing", miLista)

print (miLista[2:])

print (miLista[0:4])

print (miLista[:4])





##listaListaListas = [[[1,1],[2,2]],[[1,1],[2,2]]]
##print (listaListaListas)
##for listalista in listaListaListas:
##    for lista in listalista:
##        for elemento in lista:
##            print (elemento)
