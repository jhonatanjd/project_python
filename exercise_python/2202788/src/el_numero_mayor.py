num1=int(input("ingrese numero 1: "))
num2=int(input("ingrese numero 2: "))
num3=int(input("ingrese numero 3: "))

if num1> num2 and num1 >num3:
    print("el numero mayor es: "+str(num1))
else:
    if num2  > num3:
        print("el numero mayor es: "+str(num2))
    else:
        print("el numero mayor es: "+str(num3) )   