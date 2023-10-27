#Aprovando emprestimos:
v = float(input("Indique o valor do produto: R$"))
s = float(input("Salario do comprador "))
t = int(input("Em quanto tempo(Ano):"))
p = v / (t * 12)
m = s * 0.30
if p <= m:
    print("Emprestimo aprovado!")
else:
    print("\033[34mEmprestimo negado!")
