numero_de_testes = int(input())

magias = {
    'fire': [200, 20, 30, 50],
    'water': [300, 10, 25, 40],
    'earth': [400, 25, 55, 70],
    'air': [100, 18, 38, 60]
}

for _ in range(numero_de_testes):
    w, h, x0, y0 = map(int, input().split())
    tipo, nivel, cx, cy = input().split()
    nivel = int(nivel)
    cx = int(cx)
    cy = int(cy)

    raio = magias[tipo][nivel]

    # Encontrar o ponto mais próximo ao centro dentro do retângulo
    px = max(x0, min(cx, x0 + w))
    py = max(y0, min(cy, y0 + h))

    # Verificar se o ponto está dentro do círculo
    if (px - cx) ** 2 + (py - cy) ** 2 <= raio ** 2:
        print(magias[tipo][0])
    else:
        print(0)



