
num_ingresado = int(input("Ingrese un numero entero : "))

if num_ingresado > 0 :
    for secuencia in range(1,num_ingresado+1):
        #print(secuencia)
    
     if secuencia%5 == 0 and secuencia%3 == 0:
        print("fizzbuzz")
     elif secuencia%5 == 0:
        print("buzz")
     elif secuencia%3 == 0:
        print("fizz")
     else:
        print(secuencia)
else:
   print("caracter invalido")