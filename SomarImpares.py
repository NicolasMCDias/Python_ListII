#Ex.48:Somar impares multiplos de 3
num = int(input('insira um valor maximo:'))
soma = 0
cont = 0
for c in range(1, num + 1, 2):
  if c % 3 == 0:
    print(c, end=' ')
    cont += 1
    soma += c
print(f'\nA soma de todos os \033[32m{cont} valores é de {soma}')