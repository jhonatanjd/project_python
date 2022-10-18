nota1=int(input("ingrese su nota1: "))
nota2=int(input("ingrese su nota2: "))
nota3=int(input("ingrese su nota3: "))

prom=(nota1+nota2+nota3)/3

if prom>7:
    print("Excelente, aprobo")
else:
    if prom>=4:
        print("mmmm, regular")
    else:
        print("nooo, reprobo")     