#Custo de viagem v1.0:
dis = float(input("Distancia:"))
if dis >= 200:
    print(f"vai haver um custo de : R${dis * 0.45}")
else:
    print(f"vai haver um custo de : R${dis * 0.5}")