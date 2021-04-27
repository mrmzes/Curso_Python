denominaciones = [1,2,5,10,20,50,100,200,500,1000]

def validarmoneda(moneda,total):
    token = 0
    while token == 0:
        moneda = int(input("Con que moneda desea pagar"))
        for el in denominaciones:
            if (moneda == el & moneda <= total):
                token = 1
                return moneda
                break
                
                
horas = int (input ("Escriba las horas a pagar\n"))
if (horas < 3):
    total = 15
else:
    total = 15 + (horas-2)*10

print ("Solo acepto pago exacto")
print ("Total a pagar",total)



while total>0:
    for el in denominaciones:
        if (total%el<total):
            print ("$",el)
    moneda = 0
    moneda = validarmoneda(moneda,total)
    total -= moneda
    print ("Total a pagar",total)