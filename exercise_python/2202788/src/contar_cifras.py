numero = int (input("ingrese un numero de 2 cifras: "))

if not numero:
    print ("debe ingresar un numero")
else:
    if numero <10:
        print("el numero es de una cifra")
    else:
        if numero >9 and numero <100:
            print("el numero es de dos cifras")
        else:
             if numero >100 and numero <999:
                print ("numero es de tres cifras")    
             else: 
                print("el numero es mayor a 4 cifras")   