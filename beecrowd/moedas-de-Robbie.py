def isPrime(num):
    flag = True
    if num == 0 or num == 1:
        flag = False
        return flag
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

        if flag:
            return True
        else:
            return False


pilha_moeda = []
pilha_soma = []
quantidade_moedas = int(input())


for _ in range(quantidade_moedas):
    valor = int(input())
    pilha_moeda.append(valor)

salto = int(input())



for i in range(quantidade_moedas):
    indice = quantidade_moedas - (salto * i)

    if indice < 1:
        break
    else:
        pilha_soma.append(pilha_moeda[indice-1])


soma_total = sum(pilha_soma)


if isPrime(soma_total):
    print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
else:
    print("Bad boy! I’ll hit you.")