#LlaveTanque

cantidad=float(input("digite la cantidad de litros habida en el tanque "))

if(cantidad<250):
    print("abra la llave")
elif(cantidad>450):
    print("cierre la llave")
else:
    print("no es necesario un cambio")