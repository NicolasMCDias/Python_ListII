#Ano Bissexto:
ano = int(input("O Ano é ou não bissexto:"))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano é bissento.")
else:
    print('O ano não é bissexto.')
    