#Programa lista de listas
#Lista de lista de año, con sublista de dias de mes

año = int (input ("Escribe el año a llenar: "))

if (((año % 4 == 0) & (año % 100 != 0)) | (año % 400 == 0)):
    print ("Es año bisiesto")    
else:
    print('No es bisiesto')


#Meses de 31 dias, enero, marzo, mayo, julio
# agosto, octubre, diciembre
#1,3,5,7,8,10,12
#llenamos los meses de 31 dias

