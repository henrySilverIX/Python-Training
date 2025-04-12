valores_triangulo = input().split(' ')

lado_A = float(valores_triangulo[0])
lado_B = float(valores_triangulo[1])
lado_C = float(valores_triangulo[2])

lados = sorted([lado_A, lado_B, lado_C], reverse=True)

# Checando se é um triângulo pelas desigualdades

desig_1 = lado_A < lado_B + lado_C
desig_2 = lado_B < lado_A + lado_C
desig_3 = lado_C < lado_A + lado_B

triangulo_retangulo = lados[0]**2 == lados[1]**2 + lados[2]**2
triangulo_acutangulo = lados[0]**2 < lados[1]**2 + lados[2]**2
triangulo_obtusangulo = lados[0]**2 > lados[1]**2 + lados[2]**2

triangulo_isosceles = (lados[0] == lados[1] and lados[0] != lados[2]) or (lados[0] == lados[2] and lados[0] != lados[1]) or (lados[1] == lados[2] and lados[1] != lados[0])
triangulo_equilatero = lados[0] == lados[1] == lados[2]

classificacoes = {
    "TRIANGULO RETANGULO": triangulo_retangulo,
    "TRIANGULO ACUTANGULO": triangulo_acutangulo,
    "TRIANGULO OBTUSANGULO": triangulo_obtusangulo,
    "TRIANGULO EQUILATERO": triangulo_equilatero,
    "TRIANGULO ISOSCELES": triangulo_isosceles
}

for nome, condicao in classificacoes.items():
    print(f"{nome} e {condicao}")

if desig_1 and desig_2 and desig_3:
    for nome, condicao in classificacoes.items():
        if condicao:
            print(nome)

else:
    print("NAO FORMA TRIANGULO")