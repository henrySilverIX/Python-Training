def primos_ate(numero):
    primos = [True] * (numero + 1)
    primos[0:2] = [False, False]
    for i in range(2, int(numero ** 0.5) + 1):
        if primos[i]:
            for j in range(i*i, numero + 1, i):
                primos[j] = False
    return [i for i, primo_dif in enumerate(primos) if primo_dif]


fatores = {}
entrada = int(input())
lista_primos = primos_ate(entrada)

n = entrada  # guardando o valor original

for primo in lista_primos:
    while entrada % primo == 0:
        fatores[primo] = fatores.get(primo, 0) + 1
        entrada = entrada // primo
    if entrada == 1:
        break

# Se ainda restar um número primo maior que a raiz de entrada
if entrada > 1:
    fatores[entrada] = 1

# Construindo a saída
saida = ''.join(f"{p}({m})" for p, m in fatores.items())
print(saida)