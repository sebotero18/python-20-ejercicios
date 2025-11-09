#EcuacionCuadratica

import math

a=float(input("digite a "))
b=float(input("digite b "))
c=float(input("digite c "))

discriminante=math.sqrt((b**2)-4*a*c)

if(discriminante>=0 and a!=0):
    print("Tiene solucion")
else:
    print("No tiene solucion")
    