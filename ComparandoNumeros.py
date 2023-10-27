#Ex.38:Comparando números
n1 = int(input('primeiro valor:'))
n2 = int(input('segundo valor:'))
if n1 > n2:
  print(f'O {n1} é maior que {n2}')
elif n1 < n2:
  print(f'O {n2} é maior que {n1}')
else:
  print('Os números tem o mesmo valor')