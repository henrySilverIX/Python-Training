tempos = input().split(' ')

hora_inicial = int(tempos[0])
minuto_inicial = int(tempos[1])
hora_final = int(tempos[2])
minuto_final = int(tempos[3])


qtde_minutos_iniciais = hora_inicial * 60 + minuto_inicial
qtde_minutos_finais = hora_final * 60 + minuto_final

diferenca = qtde_minutos_finais - qtde_minutos_iniciais


if diferenca == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif diferenca < 0:
    diferenca = diferenca + 1440

    hora_resultado = diferenca // 60
    minuto_resultado = diferenca % 60

    print(f"O JOGO DUROU {hora_resultado} HORA(S) E {minuto_resultado} MINUTO(S)")

else:
    hora_resultado = diferenca // 60
    minuto_resultado = diferenca % 60
    print(f"O JOGO DUROU {hora_resultado} HORA(S) E {minuto_resultado} MINUTO(S)")
