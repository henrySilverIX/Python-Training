import math

coeficientes = input().split(' ')

coef_a = float(coeficientes[0])
coef_b = float(coeficientes[1])
coef_c = float(coeficientes[2])

delta = coef_b**2 - 4 * coef_a * coef_c

if delta >= 0 and coef_a != 0:
    R1 = (-coef_b + math.sqrt(delta)) / (2 * coef_a)
    R2 = (-coef_b - math.sqrt(delta)) / (2 * coef_a)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")

else:
    print("Impossivel calcular")



