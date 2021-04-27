#Programa para verificar frase palindroma

#Funcion para pasar un string a lista
def validarpalindromo (frase):
    frase = frase.replace(" ","")
    frasebien = []
    frasevolteada = []
    frase = frase.lower()
    for i in range(len(frase)):
        frasebien.append(frase[i])
        frasevolteada.append(frase[i])
    frasevolteada.reverse()
    
    if frasebien == frasevolteada:
        print ("Es palindromo")
    else:
        print ("No es palindromo")


validarpalindromo(input ("Ingresa la frase: "))

##    
##print (frasebien)
##print (frasevolteada)

##if frasebien == frasevolteada:
##    print ("Es palindromo")
##else:
##    print ("No es palindromo")
