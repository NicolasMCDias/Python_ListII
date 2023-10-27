#Ex.44:Gerenciador de pagamentos
preço = float(input('Insirá o valor do produto:R$'))
print('[1]Dinheiro à vista\n[2]2x no cartão\n[3]3x no cartão\n[4]à vista no cartâo')
cond_pagamento = int(input('Modo de pagamento: '))
if cond_pagamento == 1:
  des = preço - preço * (10/100)
  print(f'pagará R${des:.2f}')
elif cond_pagamento == 2:
  d = preço / 2
  print(f'2x de R${d:.2f}')
elif cond_pagamento == 3:
  des = preço + preço * (20/100)
  print(f'3x de R${des / 3:.2f}')
else:
  print(f'Pagará R${preço - preço * 0.05:.2f}')