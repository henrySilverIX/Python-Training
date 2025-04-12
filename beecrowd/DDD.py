DDD = {61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro", 32: "Juiz de Fora", 19: "Campinas", 27: "Vitoria", 31: "Belo Horizonte"}

ddd_digitado = int(input())

if ddd_digitado in DDD.keys():
    print(DDD[ddd_digitado])
else:
    print("DDD nao cadastrado")