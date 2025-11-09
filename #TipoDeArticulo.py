#TipoDeArticulo

precio=float(input("digite el valor de tu artivulo"))
descuento=str(input("digite el tipo de descuento a conocer(textil-elect-cocina-games)"))

E=precio-(precio*0.037)
C=precio-(precio*0.042)
V=precio-(precio*0.078)

if(descuento== 'textil'):
    print("el valor de tu producto no se ve afectado")
elif(descuento== 'elect'):
    print("el valor de tu producto es ",E)
elif(descuento== 'cocina'):
    print("el valor de tu producto es ",C)
elif(descuento== 'games'):
    print("el valor de tu producto es ",V)
else:
    print("no hay descuento")
    