T = int(input())

for _ in range(T):
    raios_cabos = input().split()
    valores_raios = []
    for s in raios_cabos:
        valores_raios.append(int(s))

    print(sum(valores_raios))
