#EnteroIntervalo

num=int(input("digite el número entero"))
minval=float(input("digite el número mas pequeño del intervalo "))
maxval=float(input("digite el número mas grande del intervalo "))

if(num>=minval and num<=maxval):
    print("el número está en el intervalo")
else:
    print("el número no está en el intervalo")