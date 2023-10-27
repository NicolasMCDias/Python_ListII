#Ex.34:Aumentos multiplos
sal = float(input('Qual é o valor do salario:'))
if sal <= 1250:
  print(f'agora ele passa a ser de R${sal + sal * (10 / 100):.2f}')
else:
  print(f'Agora seu salario é de R${sal + sal * (15 / 100):.2f}')