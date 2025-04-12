notas_digitadas = [x for x in input().split() if x != '']

n1 = float(notas_digitadas[0])
n2 = float(notas_digitadas[1])
n3 = float(notas_digitadas[2])
n4 = float(notas_digitadas[3])

media_final = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)

if media_final >= 7.0:
    print(f"Media: {media_final:.1f}")
    print("Aluno aprovado.")
elif media_final < 5.0:
    print(f"Media: {media_final:.1f}")
    print("Aluno reprovado.")
else:

    print(f"Media: {media_final:.1f}")
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    recalculo_nota = (nota_exame + media_final) / 2
    print(f"Aluno aprovado.\nMedia final: {recalculo_nota:.1f}" if recalculo_nota >= 5.0 else f"Aluno reprovado.\nMedia final: {recalculo_nota:.1f}")