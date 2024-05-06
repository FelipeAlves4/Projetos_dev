numero = int(input("Digite um numero: "))
con = int(input("Vc quer converter para (1)Binario (2)octal (3)hexadecimal:  "))

if con == 1 :
    print("seu numero será {}".format(bin(numero)))
elif con == 2 : 
    print("seu numero será {}".format(oct(numero)))

else: 
    print(" seu numero será {}".format(hex(numero)))
