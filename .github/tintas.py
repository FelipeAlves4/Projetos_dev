#Tintas
altura = int(input("Digite a altura: "))
largura = int(input("Digite a largura: "))
area = altura*largura
rende = area / 3
valor = 290
latas_quanti = rende/18
latas = int(latas_quanti) if latas_quanti == int(latas_quanti) else int(latas_quanti + 1)
total = (latas*valor)

print(f"Você irá precisar de {latas:.2f} latas(s)!")
print(f"Custará R${total:.2f} reais")
print(latas)
