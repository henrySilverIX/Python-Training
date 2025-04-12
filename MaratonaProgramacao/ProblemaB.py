def distribuir_pontos(a, i, p, c):
    pontos_base = p // i
    sobra = p % i

    distribuicao = []

    for posicao in range(1, i + 1):
        pontos = pontos_base
        if posicao == a:
            pontos += sobra  # o aluno da posição A recebe a sobra

        criterios = []
        for _ in range(c):
            if pontos >= 3:
                criterios.append(3)
                pontos -= 3
            else:
                criterios.append(pontos)
                pontos = 0

        distribuicao.append(criterios)

    # Imprimir resultado
    for linha in distribuicao:
        print(' '.join(map(str, linha)))


# Exemplo de uso:

entrada = input().split()
a, i, p, c = map(int, entrada)
distribuir_pontos(a, i, p, c)