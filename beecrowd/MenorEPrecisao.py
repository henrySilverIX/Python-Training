N = int(input())

X = []

numeros = input().split()

for s in numeros:
    X.append(int(s))

menor_valor = X[0]
posicao = 0

for k in range(N-1):
    if X[k] <= menor_valor:
        menor_valor = X[k]
        posicao = k

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")