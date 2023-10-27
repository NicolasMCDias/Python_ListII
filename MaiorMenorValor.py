#Ex.33:Maior e Menor valores
a = float(input('Insirá o 1° valor:'))
b = float(input('Insirá o 2° valor:'))
c = float(input('Insirá o 3° valor:'))
menor = c
if a < b and a < c:
  menor = a
if b < c and b < a:
  menor = b
maior = c
if a>b and a>c:
  maior = a
if b < c and b < a:
  maior = b
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')