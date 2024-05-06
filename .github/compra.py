print("{:=^40}".format(" Lojas Felipe "))

compra = float(input("Qual o valor da compra? R$"))
print('''Formas de pagamento
 [1]check/a vista dinheiro
 [2] a vista cartão 
 [3] 2x no cartão
 [4] 3x no cartão ou mais''')
opçao = int(input("Qual seria a opção? "))

if opçao == 1:
    total= compra*0.9
   

elif  opçao == 2:
    total = compra*0.95

elif opçao == 3:
    total = compra
    parcela = total / 2 
    print(f"Sua compra de R${total} vai ficar em 2x por mês, com parcelas de R${parcela}")

elif opçao == 4: 
    total = compra + (compra * 20/100)
    totalpa = int(input("Em quantas parcelas deseja pagar? "))
    parcela = total / totalpa
    print(f"Sua compra será parcelada em {totalpa} e ficará R${parcela} por mês")
else: 
 total = 0
 print("Opção invalida de pagamento. Tente novamente")
 
print("sua compra de R${} vai custar no final  R${}".format(compra,total))
