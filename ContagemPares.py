#Ex.47:Contagem de pares
num = int(input('coloque o numero maximo e forneceremos os pares:'))
for n in range(1, num):
  if n % 2 == 0:
    print(n, end=' ')
print('FIM!')