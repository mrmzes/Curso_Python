#Programa para verificar frase palindroma
frase = input ("Ingresa la frase: ")
frase = frase.replace(" ","")
frasebien = []
frasevolteada = []
frase = frase.lower()

#guardamos la frase en una lista
for i in range(len(frase)):
    frasebien.append(frase[i])
    frasevolteada.append(frase[i])
frasevolteada.reverse()
print (frasebien)
print (frasevolteada)

if frasebien == frasevolteada:
    print ("Es palindromo")
else:
    print ("No es palindromo")
