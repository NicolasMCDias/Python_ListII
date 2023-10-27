#RADAR ELETRONICO:
velocidade = float(input("Velocidade do veiculo[Km]: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("-=-" * 15)
    print("VOCÊ FOI MULTADO!!\nVALOR DA MULTA: R$ {:.2f}".format(multa))