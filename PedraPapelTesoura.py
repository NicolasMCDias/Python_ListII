#Ex.45:Pedra, papel e tesoura
from random import randint
print('[0]pedra\n[1]papel\n[2]tesoura')
items = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0,2)
player = int(input('coloque o valor: '))
print(f'Computador jogou {items[comp]}')
print(f'Player jogou {items[player]} ')
if comp == 0:
  if player == 0:
    print('Empate')
  elif player == 1:
    print('Player Venceu!')
  elif player == 2:
    print('Player Perdeu!')
  else:
    print('Jogada invalida')    
elif comp == 1:
  if player == 0:
    print('Player Perdeu!')
  elif player == 1:
    print('empate')
  elif player == 2:
    print('Player Venceu!')
  else:
    print('Jogada invalida')
elif comp == 2:
  if player == 0:
    print('Player Venceu!')
  elif player == 1:
    print('Player Perdeu!')
  elif player == 2:
    print('empate')
  else:('Jogada invalida')
