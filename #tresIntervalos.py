#tresIntervalos

num=float(input("digite el número"))
minval1=float(input("digite el valor minimo del primer intervalo"))
maxval1=float(input("digite el valor maximo del primer intervalo"))
minval2=float(input("digite el valor minimo del segundo intervalo"))
maxval2=float(input("digite el valor maximo del segundo intervalo"))
minval3=float(input("digite el valor minimo del tercer intervalo"))
maxval3=float(input("digite el valor maximo del tercer intervalo"))

if(num>minval1 and num<maxval1 or num>minval2 and num<maxval2 or num>minval3 and num<maxval3):
    print("el valor está en uno de los intervalos")
else:
    print("el valor no está dentro de los intervalos")