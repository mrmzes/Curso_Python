def fun (num1, num2):
    if num1 == 1:
        return num1 + num2
    elif num1 == 5:
        return "El primer número es 5"
      
def arginf(*arg):
  print ("Funcion llamada con ", len(arg), "argumentos:", arg, "de tipo: ", type(arg))
  print (fun(arg[0],arg[1]))

  
  
arginf (1,2,3,"Nombre")
arginf (2.22,5)
arginf (5,0,0,0)
arginf (2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
