#MayorDeCuatro

n1=float(input("digite el primer número "))
n2=float(input("digite el segundo número "))
n3=float(input("digite el tercer número "))
n4=float(input("digite el cuarto número "))

if(n1==n2 and n1==n3 and n1==n4 and n2==n3 and n2==n4 and n3==n4):
    print("son iguales")
elif(n1>=n2 and n1>=n3 and n1>=n4):
    print("el ",n1," es el mayor")
elif(n2>=n1 and n2>=n3 and n2>=n4):
    print("el ",n2," es el mayor")
elif(n3>=n1 and n3>=n2 and n3>=n4):
    print("el ",n3," es el mayor")
else:
    print("el ",n4," es el mayor")
    
