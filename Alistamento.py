#Ex.39:Alistamento militar
from datetime import date
atual = date.today().year
nacimento = int(input('Coloque o ano que naceu:'))
alistamento = atual - nacimento
if alistamento == 18:
  print('Está no ano de se alistar')
if alistamento < 18:
  print(f'faltam {18 - alistamento} anos para se alistar')
if alistamento > 18:
  print(f'você deveria ter se alistado a {alistamento - 18} anos atrás')