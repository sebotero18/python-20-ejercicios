#SoldadoAptoONoApto

genero=str(input("digite su genero (F o M) "))
estatura=float(input("digite su estatura en Cm "))
edad=float(input("digite su edad "))
estadoCivil=str(input("digite su estado civil (S o C) "))

if(estadoCivil=='S' and genero=='F' and estatura>=160 and edad>=20 and edad<=25 ):
    print("es apta")

elif(estadoCivil=='S' and genero=='M' and estatura>=165 and edad>=18 and edad<=24 ):
    print("es apto")
    
else:
    print("no es apto")

    
    


