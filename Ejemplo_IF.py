#ESTE CODIGO SACA PROMEDIO DE LAS CALIFICACIONES
print('\nPROMEDIO DEL SEMESTRE\n')
#INGRESA CALIFICACIONES
calif1 = float(input('CALIFICACION PARCIAL 1: '))
calif2 = float(input('CALIFICACION PARCIAL 2: '))
calif3 = float(input('CALIFICACION PARCIAL 3: '))
calif4 = float(input('CALIFICACION PARCIAL 4: '))
calif5 = float(input('CALIFICACION PARCIAL 5: '))
#CALCULAR PROMEDIO
promedio = (calif1+calif2+calif3+calif4+calif5)/5
#IMPRIME EL PROMEDIO
if(promedio>=7 and promedio<=10):
    print('Tu promedio es ',promedio, ' Aprobaste')
elif(promedio>=0 and promedio<7):
    print('Tu promedio es ',promedio, ' Reprobaste')
else:
    print('Calificación no es valida')

