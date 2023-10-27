#Ex.50:Soma de pares
num = int(input('valor maximo: '))
soma = 0
for n in range(1,num + 1):
  if n % 2 == 0:
    print(n)
    soma += n
print(f'soma = {soma}')