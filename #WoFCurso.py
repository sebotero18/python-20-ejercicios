#WoFCurso

n1 = float(input("Digite la nota de su primer trabajo "))
n2 = float(input("Digite la nota de su segundo trabajo "))
n3 = float(input("Digite la nota de su tercer trabajo "))
n4 = float(input("Digite la nota de su cuarto trabajo "))
n5 = float(input("Digite la nota de su quinto trabajo "))

promedio = (n1 + n2 + n3 + n4 + n5) / 5

if(promedio>=3.5):
    print(promedio," Pasó el curso")
else:
    print(promedio," No pasó el curso")
