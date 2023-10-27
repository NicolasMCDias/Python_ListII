#Ex.40:Aquele classico da media
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
if media <= 5:
  print('reprovado')
elif 5 < media <= 6.9:
  print('recuperação')
elif media >= 7:
  print('aprovado')