C = int(input())

T = input()
soma = 0

tamanho_vetor = 12

M = []

for i in range(tamanho_vetor):
    linha = []
    for j in range(tamanho_vetor):
        valor = float(input())
        linha.append(valor)
    M.append(linha)



if T == 'S':
    for i in range(tamanho_vetor):
        soma += M[i][C]
    print(soma)
else:
    for i in range(tamanho_vetor):
        soma += M[i][C]
    print(f"{soma/tamanho_vetor:.1f}")