#Ex.42:Analisando triângulos v2.0
from time import sleep
a = float(input('segmento â: '))
b = float(input('segmento b: '))
c = float(input('segmento c: '))
if a > b + c or b > a + c or c > a + b:
  print('Não forma um triângulo')
else:
  print('Forma um triângulo...')
  sleep(2)
  if a == b == c:
    print('Equilatero')
  elif a != b != c:
    print('Escaleno')
  else:
    print('Isóceles')