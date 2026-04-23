T = input()
soma = 0

tamanho_vetor = 12
denominador_media = 66

M = []

for i in range(tamanho_vetor):
    linha = []
    for j in range(tamanho_vetor):
        valor = float(input())
        linha.append(valor)
    M.append(linha)


if T == 'S':
    for i in range(tamanho_vetor):
        for j in range(tamanho_vetor):
            if j > i:
                soma += M[i][j]
    print(soma)
else:
    for i in range(tamanho_vetor):
        for j in range(tamanho_vetor):
            if j > i:
                soma += M[i][j]
    print(f"{soma/denominador_media:.1f}")