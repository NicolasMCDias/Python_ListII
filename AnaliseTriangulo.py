#Analise de triangulo:
a = float(input('Segmento A:'))
b = float(input('Segmento B: '))
c = float(input("Segmento C"))

if a > b + c or b > a + c or c > a + b:
    print("Não é possivel os segmentos formarem um triângulo.")
else:
    print("É possivel a formação de um triangulo com os segmentos apresentados.")
    