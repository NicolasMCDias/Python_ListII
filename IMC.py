#Ex.43:Indice de massa corporal
peso = float(input('coloque seu peso: '))
h = float(input('agora a altura: '))
IMC = peso / h ** 2
print(f'Seu IMC é de {IMC:.2f} assim sendo classificado como: ')
if IMC < 18.5:
  print('Abaixo do peso')
elif 18.5 < IMC <= 25:
  print('Peso ideal')
elif 25.1 <= IMC <= 30:
  print('Sorbrepeso')
elif 30.1 <= IMC <= 40:
  print('Obesidade')
elif IMC > 40:
  print('Obesidade morbida')