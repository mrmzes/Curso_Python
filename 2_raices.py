A=float(input("Dar el coeficiente de la x cuadrada "))
if (A != 0):
    B=float(input("Dar el coeficiente de la x "))
    C=float(input("Dar el valor de la constante "))
    D=(B*B)-(4*A*C)
    if (D>=0):
        X1=(-1*B+(D**.5))/(2*A)
        X2=(-1*B-(D**.5))/(2*A)
        print("\n\nLas raices reales son " + str(X1)+ " y " + str(X2))
    else:
        REAL = -1*B / (2*A)
        IMAG = ((-1*D)**.5)/(2*A)
        COM = REAL + IMAG 
        print ("\n\nLa primer raiz imaginaria es " + str(REAL) + " + " + str(IMAG) + " i")
        print ("\nLa segunda raiz imaginaria es " + str(REAL) + " - " + str(IMAG) + " i")
else:
    print ("No es una ecuación cuadratica")

