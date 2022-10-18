numero1=int(input("digite eje x"))
numero2=int(input("digite eje y"))


if numero1 <= -1 and numero2>=1:
    print("el punto esta en el primer cuadro")
else:
    if numero1>=1 and numero2>=1:
        print("el punto esta en el segundo cuadro")
    else: 
        if numero1<=-1 and numero2<=-1:
            print("el punto est en el cuarto cuadro")
        else:
            if numero1>=1 and numero2<=-1:
                print("el punto estae en el tercer cuadro")
            

