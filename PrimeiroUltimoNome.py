#Ex.27:primeiro e ultumo nome de uma pessoa
nome = input('insira o nome completo:').strip().title()
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]}')
print(f'SEu último nome é {separa[-1]}')