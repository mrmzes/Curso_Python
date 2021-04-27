contraseña = "abc123"
count = 0
while (contraseña != input("Escribe tu contraseña\n")) & (count<3):
    print ("Contraseña invalida")
    count += 1
    print ("Intentos ", count)
