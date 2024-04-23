#raiz quadrada, plano cartesiano

X1,Y1 = input().split(" ")
x1 = int(X1)
y1 =  int(Y1)

X2,Y2 = input().split(" ")
x2 = int(X2)
y2 = int(Y2)

a = (x2 - x1)**2
b = (y2 - y1)**2
c = (a + b)
d = (c ** 0.5)
print(f"{d:.4f}")
