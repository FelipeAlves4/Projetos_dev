from datetime import date

atual = date.today().year

ano =  int(input("Digite o ano q nasceu: "))
idade =  atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

if idade == 18: 
    print("Vc tem que se alistar imediatamente!")
elif idade < 18: 
    saldo =  18 - idade 
    print("Vc ainda n tem 18 anos. Ainda faltam {} anos".format(saldo))
    ira =  atual + saldo 
    print("Seu alistamento irá ser em {}".format(ira))
else:
    saldo = idade - 18 
    print("Vc ja devia ter se alistado a {} anos ".format(saldo))
    ira =  atual - saldo 
    print("Seu alistamento deveria ter sido em {}".format(ira))
