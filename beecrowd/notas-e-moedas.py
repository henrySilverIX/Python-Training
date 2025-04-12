from decimal import Decimal, ROUND_DOWN

valor = Decimal(input()).quantize(Decimal('0.01'), rounding = ROUND_DOWN)

valor_para_centavos = int(valor*100)

cedulas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]
quantidades_cedulas = []
quantidades_moedas = []


#Cálculo para as cédulas
for notas in cedulas:
    if valor_para_centavos // notas != 0:
        quantidades_cedulas.append(valor_para_centavos//notas)
        valor_para_centavos = valor_para_centavos % notas
    else:
        quantidades_cedulas.append(0)


for moeda in moedas:
    if valor_para_centavos // moeda != 0:
        quantidades_moedas.append(int(valor_para_centavos // moeda))
        valor_para_centavos = valor_para_centavos % moeda
    else:
        quantidades_moedas.append(0)


print("NOTAS:")
for qtde,notas in zip(quantidades_cedulas, cedulas):
    print(f"{int(qtde)} nota(s) de R$ {notas/100:.2f}")

print("MOEDAS:")
for qtde_moedas, moeda in zip(quantidades_moedas, moedas):
    print(f"{qtde_moedas} moeda(s) de R$ {moeda/100:.2f}")

