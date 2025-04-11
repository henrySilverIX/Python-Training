salario = float(input())

if salario <= 2000.00:
    print("Isento")
elif 2000.00 < salario <= 3000.00:
    total = (salario - 2000.00) * 0.08
    print(f"R$ {total:.2f}")

elif 3000.00< salario <= 4500.00:
    valor_para_imposto = salario - 2000.00
    total = (1000 * 0.08) + ((valor_para_imposto - 1000.00) * 0.18)
    print(f"R$ {total:.2f}")

else:
    valor_para_imposto = salario - 2000.00
    total = (1000.00 * 0.08) + (1500.00 * 0.18) + ((valor_para_imposto - 2500.00) * 0.28)
    print(f"R$ {total:.2f}")
