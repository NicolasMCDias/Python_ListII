#Ex.41:Classificando atletas
idade = int(input('Insirá sua idade: '))
if idade <= 9:
  print('MIRIM')
elif 9 < idade <= 14:
  print('INFANTIL')
elif 14 < idade <= 19:
  print('JUNIOR')
elif 19 < idade <= 24:
  print('SENIOR')
else:
  print('MASTER')