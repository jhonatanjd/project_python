#x=1
#while x<=100:
 #   print(x)
  #  x=x+1

#num1= int(input("digite el valor final" "\n"))
#x=1
#.
# while x<=num1:
#    print(x)
#    x=x+1
#v=1
#suma =0
#while v<=10:
 #   num= int(input("digite un numero: "))
  #  print(num)
   # suma = suma+num
  #  v = v+1
#prom = suma/10
#print("la suma es: " +str(suma))
#print ("el promedio es: " +str(prom))

mayores=0
menores=0
x=1
suma=0
while x<=10:
  num= int(input("digite los  numeros: "+str(x)+ "\n"))
  x+=1
  suma=+num
  if num>=5:
    mayores+=5
  else:
    menores-=1
print("la suma de los numeros es : "+str(suma))
print("el promedio es:"+str(suma/10))
print("los numeros mayores a 5 son: "+str(mayores))
print("los numeros menores a 5 son: "+str(menores))











