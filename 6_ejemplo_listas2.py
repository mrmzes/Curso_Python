print ("Imprime mi lista")
miLista = [0,1,1,2,3,5]
print (miLista)
input ()

print ("Agregar 'añadido' a la lista")
miLista.append("añadido")
print (miLista)
input ()

print ("Inserta 'insertado' en el indice '2'")
miLista.insert(2,"insertado")
print (miLista)
input ()

print ("Remueve el valor 'añadido' de la lista")
miLista.remove ("añadido")
print (miLista)
input ()

print ("Remueve el primer '1' en la lista")
miLista.remove (1)
print (miLista)
input ()


print ("Se va a remover: ", miLista.pop(2))
input ("Se muestra y elimina")
print (miLista)
input ()


print ("Regresa el indice de 'insertado'")
print ( miLista.index("insertado") )
input ()

for elemento in miLista:
    print (elemento, " es de tipo", type(elemento))

input ()
print ("Limpia la lista")
miLista.clear()
print (miLista)
input()


nuevaLista = [20,30,40,10,100,98,70,70,78,79,]
print ("Hay ",nuevaLista.count(70)," repeticiones de '70' en la lista nueva")
print (nuevaLista)
input()

print ("Ordena la lista")
nuevaLista.sort()
print (nuevaLista)
input()

print ("Orden inverso de lista")
nuevaLista.sort (reverse = True)
print (nuevaLista)
input()

print ("Otra manera de invertir la lista")
nuevaLista.reverse()
print (nuevaLista)
input()


print ("Elimina el elemento '0' de la lista")
del nuevaLista[0]
print (nuevaLista)
input()

print ("Elimina los elemntos '2:4' de la lista")
del nuevaLista[2:4]
print (nuevaLista)
input()

print ("Elimina la lista")
del nuevaLista[:]
print (nuevaLista)
