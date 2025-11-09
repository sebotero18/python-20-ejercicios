#Descuentos

num=float(input("digite el valor de su articulo"))

descuento=int(input("digite el tipo de descuento"))

desc1=num-(num*0.125)
desc2=num-(num*0.083)
desc3=num-(num*0.032)

if (descuento==1):
    print("el valor de tu articulo con el descuento tipo 1 es ",desc1)
elif (descuento==2):
    print("el valor de tu articulo con el descuento tipo 2 es ",desc2)
elif (descuento==3):
    print("el valor de tu articulo con el descuento tipo 3 es ",desc3)
else:
    print("el articulo no se ve afectado por ningun descuento ", num)
