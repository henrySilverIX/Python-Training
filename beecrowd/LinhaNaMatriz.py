L = int(input())

T = input()
soma = 0

M = []

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    M.append(linha)



if T == 'S':
    for i in range(12):
        soma += M[L][i]
    print(soma)
else:
    for i in range(12):
        soma += M[L][i]
    print(soma/12)
