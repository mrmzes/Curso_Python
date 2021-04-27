contr = input ("escribe alguna contraseña: ")
contraseña = ""
##hay que leer elemento por elemento
##luego hacer un if por a,A,e,E,i,I,o,O

lista = []

for i in range (len(contr)):
    if (contr[i] == "a") | (contr[i] == "A"):
        lista.append ("@")
    elif (contr[i] == "e") | (contr[i] == "E"):
        lista.append ("3")
    elif (contr[i] == "i") | (contr[i] == "I"):
        lista.append ("1")
    elif (contr[i] == "o") | (contr[i] == "O"):
        lista.append ("0")
    else:
        lista.append(contr[i])


for i in range (len(contr)):
    contraseña += lista[i]


print (contraseña)
#otra vez recorrer la lista
#con un if


